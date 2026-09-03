# Split Summary — For Approval Before Modeling

Run ID: `20260903T042027Z` | Pipeline v1.0 | seed `20260903`
Input: `bcfdb.csv`, sha256[:16] `fe54767e0054c1ee`, 6,679 raw rows

## 1. Filtering funnel (exact counts)

| Step | Rows remaining | Removed | Reason |
|---|---|---|---|
| Raw file loaded | 6,679 | — | — |
| Invalid/missing BCF removed | 6,578 | 101 | bcf null or <= 0, cannot log-transform or model |
| → SOURCE domain | 2,349 | — | `soil_type == 'spiked'` |
| → TARGET domain | 3,352 | — | `soil_type in {polluted, natural, natural clean}` AND `spiked_soil == False` |
| → EXCLUDED (supplementary) | 877 | — | see breakdown below |

Partition sum check: 2,349 + 3,352 + 877 = 6,578. ✓

**Exclusion breakdown (877 rows, all preserved in `excluded_supplementary.csv`, none discarded):**
| Reason | Rows |
|---|---|
| Amended soil (confounded manipulation) | 472 |
| Hybrid: spiked onto already-polluted soil | 251 |
| Ambiguous: missing `spiked_soil` flag | 138 |
| Missing `soil_type` | 15 |
| Commercial substrate | 1 |
| **Total** | **877** |

## 2. Domain sizes and CV structure

- **SOURCE (train/val):** 2,349 rows, 88 studies
- **TARGET (frozen test, domain-shift eval):** 3,352 rows, 140 studies
- **5-fold grouped CV on SOURCE**, grouped by `doi`: fold sizes 469/469/471/471/469, studies-per-fold 15/17/18/19/19. Verified: zero studies span more than one fold.

## 3. Cross-domain robustness subset (predefined, per your instruction)

**15 studies** contribute rows to both SOURCE and TARGET (257 total rows across both domains). This is one fewer than the 16 identified in the earlier exploratory pass, because this number is now computed after applying the full locked protocol and the invalid-BCF filter, which is the correct final figure. Full list in `run_manifest_latest.json` and `tables/cross_domain_robustness_subset.csv`. This subset is reserved for the predefined within-study robustness analysis: for these 15 studies only, compare source-condition vs. target-condition BCF within the same lab/methodology, isolating the domain effect from between-study noise as far as the data allows.

## 4. Feature schema (26 raw columns classified, 8 usable as model features)

**Explicitly banned as predictive features** (enforced and verified in the leakage audit):
- `chemical_form` — 45.6% missing in source vs. 99.9% missing in target; structurally tautological with domain
- `oxidative_state` — 88.7% / 99.2% missing; same problem
- `soil_type` — this is the domain-definition field itself; using it as a feature would let the model trivially detect domain rather than learn transferable chemistry

**Also excluded, different reason:**
- `plant_concentration` — bcf is derived from this; including it leaks the target
- `spiked_soil`, `natural_soil` — used only to define the split, not as inputs
- `doi` — used only as the CV grouping key
- High-missingness / unstructured fields: `variety`, `location`, `date`, `treatment`, `irrigation`, `fertilization`, `notes`, `concentration_units`

**Usable features:** `species`, `element` (+ engineered atomic number, atomic mass, electronegativity, ionic radius from a static lookup table, all 27 present elements covered), `plant_component`, `soil_ph`, `organic_matter_pct`, `soil_concentration`, `dry_weight`, `duration_days` — numeric fields get missingness indicators plus median imputation within species × element, per the design doc.

Full column-by-column classification: `tables/feature_schema.csv`.

## 5. Leakage audit: 7/7 checks passed

All banned columns confirmed excluded, no row duplicated across source/target, every study assigned to exactly one CV fold, cross-domain study list internally consistent. Full detail: `outputs/leakage_audit_latest.json`.

## 6. Target distribution (for reference, full numbers in `tables/audit_log_bcf_summary_by_domain.csv`)

Source median log10(BCF) ≈ -0.16, target median ≈ -0.59 (consistent with the earlier exploratory audit; exact values recomputed on the final filtered partitions are in the table).

## 7. What is NOT done yet

No model has been trained. No feature scaling/imputation has been fit. The external validation set has not been touched. This document, plus the artifacts in `tables/` and `outputs/logs/`, is the checkpoint for your review before any of that proceeds.

## Files produced this run

```
outputs/
  run_manifest_20260903T042027Z.json      run_manifest_latest.json
  leakage_audit_latest.json
  logs/01_clean_and_split_*.log            logs/02_feature_schema_*.log
  tables/
    cleaned_dataset_full.csv               source_domain.csv
    target_domain.csv                      excluded_supplementary.csv
    invalid_bcf_excluded.csv               cross_domain_robustness_subset.csv
    feature_schema.csv                     element_property_lookup.csv
    audit_study_by_domain.csv              audit_element_by_domain.csv
    audit_species_by_domain.csv            audit_plant_component_by_domain.csv
    audit_log_bcf_summary_by_domain.csv    audit_missingness_by_domain.csv
    audit_element_by_species_by_domain.csv
```
