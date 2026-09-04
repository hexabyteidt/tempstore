"""
Overlap audit: run this against the manually populated external CSV before
freezing it, and again as the final check before hashing.

Never declares independence just because a DOI string differs. Flags
possible/probable overlap for human judgment; it does not resolve
ambiguous cases itself.

Usage:
    python overlap_audit_script.py --external path/to/external.csv \
        --primary /home/claude/pipeline/outputs/tables/cleaned_dataset_full.csv \
        --out overlap_audit_report.json
"""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

SCRIPT_VERSION = "v1.0"


def normalize_doi(doi):
    if pd.isna(doi):
        return None
    d = str(doi).strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = re.sub(r"\s+", "", d)
    return d if d else None


def is_malformed_doi(doi):
    if doi is None:
        return True
    # a real DOI starts with "10." and has a slash after the prefix
    return not re.match(r"^10\.\d{4,9}/\S+$", doi)


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run_audit(external_path, primary_path, out_path):
    report = {
        "script_version": SCRIPT_VERSION,
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "external_file": str(external_path),
        "external_file_sha256": file_hash(external_path),
        "primary_file": str(primary_path),
        "primary_file_sha256": file_hash(primary_path),
    }

    ext = pd.read_csv(external_path)
    prim = pd.read_csv(primary_path)

    # ------------------------------------------------------------------
    # 1. Malformed / missing DOI check
    # ------------------------------------------------------------------
    ext["_doi_norm"] = ext["doi"].apply(normalize_doi)
    missing_doi = ext["_doi_norm"].isna().sum()
    malformed = ext["_doi_norm"].apply(
        lambda d: (not pd.isna(d)) and is_malformed_doi(d)
    ).sum()
    report["missing_doi_count"] = int(missing_doi)
    report["malformed_doi_count"] = int(malformed)
    if missing_doi > 0:
        report["missing_doi_rows"] = ext.loc[ext["_doi_norm"].isna(), "study_id"].tolist() \
            if "study_id" in ext.columns else ext.index[ext["_doi_norm"].isna()].tolist()

    # ------------------------------------------------------------------
    # 2. Exact and normalized DOI overlap against primary dataset
    # ------------------------------------------------------------------
    prim_dois = set(prim["doi"].dropna().apply(normalize_doi))
    ext["_confirmed_doi_overlap"] = ext["_doi_norm"].isin(prim_dois)
    confirmed_overlap_rows = ext.loc[ext["_confirmed_doi_overlap"]]
    report["confirmed_doi_overlap_count"] = int(len(confirmed_overlap_rows))
    report["confirmed_doi_overlap_dois"] = sorted(
        confirmed_overlap_rows["_doi_norm"].dropna().unique().tolist()
    )

    # ------------------------------------------------------------------
    # 3. Probable overlap: same species + element + similar soil
    #    concentration as an existing primary-dataset row, even with a
    #    different DOI (possible republication / reused dataset). This is
    #    a heuristic flag, not a determination -- always requires human
    #    review, per the "different DOI does not mean independent" rule.
    # ------------------------------------------------------------------
    probable_overlap_flags = []
    if {"species", "element", "soil_concentration"}.issubset(ext.columns) and \
       {"species", "element", "soil_concentration"}.issubset(prim.columns):
        for idx, row in ext.iterrows():
            if row["_confirmed_doi_overlap"]:
                continue
            if pd.isna(row.get("species")) or pd.isna(row.get("element")):
                continue
            candidates = prim[
                (prim["species"] == row["species"]) &
                (prim["element"] == row["element"])
            ]
            if len(candidates) == 0:
                continue
            sc = row.get("soil_concentration")
            if pd.notna(sc) and "soil_concentration" in candidates.columns:
                close = candidates[
                    (candidates["soil_concentration"] - sc).abs() /
                    candidates["soil_concentration"].abs().clip(lower=1e-9) < 0.02
                ]
                if len(close) > 0:
                    probable_overlap_flags.append({
                        "external_row_index": int(idx),
                        "external_doi": row.get("doi"),
                        "species": row.get("species"),
                        "element": row.get("element"),
                        "soil_concentration": sc,
                        "matched_primary_dois": close["doi"].unique().tolist(),
                        "reason": "species+element+soil_concentration within 2% of an "
                                  "existing primary-dataset row under a different DOI; "
                                  "possible republished or reused experiment, requires "
                                  "manual review, not auto-excluded",
                    })
    report["probable_overlap_flags"] = probable_overlap_flags
    report["probable_overlap_count"] = len(probable_overlap_flags)

    # ------------------------------------------------------------------
    # 4. Species/element combinations present in both datasets (context,
    #    not itself a problem -- overlap in coverage is expected and fine,
    #    only row-level duplication is the concern)
    # ------------------------------------------------------------------
    if {"species", "element"}.issubset(ext.columns):
        ext_combos = set(zip(ext["species"].dropna(), ext["element"].dropna()))
        prim_combos = set(zip(prim["species"].dropna(), prim["element"].dropna()))
        shared_combos = ext_combos & prim_combos
        report["shared_species_element_combos"] = [
            {"species": s, "element": e} for s, e in sorted(shared_combos)
        ]

    # ------------------------------------------------------------------
    # 5. Duplicate rows within the external set itself
    # ------------------------------------------------------------------
    dup_cols = [c for c in ["doi", "species", "element", "plant_component",
                             "BCF_value"] if c in ext.columns]
    if dup_cols:
        dup_mask = ext.duplicated(subset=dup_cols, keep=False)
        report["internal_duplicate_count"] = int(dup_mask.sum())
        if dup_mask.sum() > 0:
            report["internal_duplicate_rows"] = ext.loc[dup_mask, dup_cols].to_dict("records")

    # ------------------------------------------------------------------
    # 6. Verification-state gate: nothing unverified should be in a
    #    "frozen" file passed to this script at freeze time
    # ------------------------------------------------------------------
    if "verification_status" in ext.columns:
        vc = ext["verification_status"].value_counts(dropna=False).to_dict()
        report["verification_status_counts"] = {str(k): int(v) for k, v in vc.items()}
        unverified = ext["verification_status"].isin(["unverified", None]) | ext["verification_status"].isna()
        report["unverified_rows_present"] = bool(unverified.any())
        report["unverified_row_count"] = int(unverified.sum())

    # ------------------------------------------------------------------
    # Overall verdict (advisory only, does not auto-decide anything)
    # ------------------------------------------------------------------
    verdict_flags = []
    if report["confirmed_doi_overlap_count"] > 0:
        verdict_flags.append("CONFIRMED DOI overlap present -- these rows must be removed "
                              "or explicitly justified before freezing.")
    if report["probable_overlap_count"] > 0:
        verdict_flags.append("Probable overlap flags present -- manual review required "
                              "before freezing.")
    if report.get("unverified_rows_present"):
        verdict_flags.append("Unverified rows present -- do not freeze until resolved.")
    if report["malformed_doi_count"] > 0 or report["missing_doi_count"] > 0:
        verdict_flags.append("Malformed or missing DOIs present -- fix before freezing.")
    report["verdict_flags"] = verdict_flags
    report["clear_to_freeze"] = len(verdict_flags) == 0

    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)

    print(json.dumps({k: v for k, v in report.items() if k not in
                       ["probable_overlap_flags", "internal_duplicate_rows",
                        "shared_species_element_combos"]}, indent=2, default=str))
    print(f"\nFull report written to {out_path}")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", required=True, type=Path)
    parser.add_argument("--primary", required=True, type=Path)
    parser.add_argument("--out", default="overlap_audit_report.json", type=Path)
    args = parser.parse_args()

    if not args.external.exists():
        print(f"External file not found: {args.external}", file=sys.stderr)
        sys.exit(1)
    if not args.primary.exists():
        print(f"Primary file not found: {args.primary}", file=sys.stderr)
        sys.exit(1)

    run_audit(args.external, args.primary, args.out)
