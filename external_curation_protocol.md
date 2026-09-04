# External Validation Curation Protocol

This protocol governs how candidate studies become verified rows in the frozen external validation set. Candidate discovery (already done, see `candidate_studies_list.csv`) and verification (your job, using this protocol) are separate stages on purpose. Nothing in the candidate list is data. It is a reading list.

## 1. Identifying candidate papers

Candidates so far came from targeted web searches per species (hemp, castor bean, bamboo, sunflower) combined with "bioconcentration factor," "phytoremediation," and year filters favoring 2023 onward. Continue this by:
- Searching each species name plus the specific element(s) underrepresented in the primary dataset (check `pipeline/outputs/tables/audit_element_by_domain.csv` for low-count elements).
- Checking the reference lists of recent review articles (e.g., the Ansari et al. 2026 hemp review flagged in the candidate list) for primary studies the review cites, since reviews aggregate exactly the kind of primary literature you need, but their own numbers must never be extracted directly.
- Checking "cited by" lists on Google Scholar for the original Ha et al. 2025 paper and for Shi et al. 2023, since papers citing either are likely to be recent and topically adjacent.

## 2. Accessing and inspecting the primary source

- Always locate the actual publisher page or PDF, not a snippet, abstract-only listing, or AI-generated summary.
- If you only have institutional or personal access to a paywalled paper, that is fine, but note `data_source_type` as "paywalled, accessed via [institution/library]" for your own records.
- If a paper is genuinely inaccessible to you, mark `eligibility_status = requires_manual_verification` and `notes = primary source inaccessible`, and leave every numeric field blank. Do not extract from the abstract alone; abstracts frequently round, average, or omit the specific numbers needed.

## 3. Verifying study independence from Ha et al. (2025)

Before extracting anything:
1. Check the exact DOI against `pipeline/outputs/tables/cleaned_dataset_full.csv`'s `doi` column (case-insensitive, trimmed). The `overlap_audit_script.py` automates this, but do it by eye too for anything the script flags as ambiguous.
2. If the DOI doesn't match, still check: same first author, same research group/institution, same field site or mine/location named in the methods, overlapping sample collection dates. A follow-up paper analyzing the same field trial under a new DOI is not independent data, even though it will pass a naive DOI check.
3. If a paper's methods section references "as described in [citation]" pointing to a study already in the primary dataset, treat it as a likely-derivative and flag for manual review rather than assuming independence.
4. Record your reasoning in `notes`, not just a status flag, so a reader (or future you) can see why a judgment call was made.

## 4. Determining genuine relevance

A candidate is relevant only if it reports BCF (or the raw numerator/denominator needed to compute it) for one of the four species (sunflower, hemp, castor bean, bamboo) and at least one metal/metalloid, in a soil-based system. Hydroponic-only or purely in-vitro studies are not directly comparable to a soil BCF and should be marked `requires_manual_verification` with the incompatibility noted, not silently included.

## 5. Identifying BCF values

Locate the actual number in a table or in-text result, not a plotted figure, if you have a choice. Note the exact table/figure number and page in `data_source_location`.

## 6. Verifying the BCF definition

This is the step most likely to silently break comparability. For every candidate:
- Find the paper's own stated formula for BCF (usually in the methods section).
- Record it verbatim (or close to verbatim) in `BCF_definition`.
- Identify numerator and denominator explicitly: is it shoot concentration / soil concentration? Whole-plant / soil? Root / soil? Record in `BCF_numerator` and `BCF_denominator`.
- Record the units used for each (mg/kg dry weight is standard but verify; some papers use fresh weight, which is not directly comparable without conversion you should not attempt silently).
- If the paper calls something "BCF" but it's actually a translocation factor, enrichment factor, or a different ratio, do not relabel it as BCF. Mark `eligibility_status = ineligible` and explain in `exclusion_reason`.
- If ambiguous (e.g., unclear whether "plant concentration" means whole-plant or a specific organ), mark `requires_manual_verification` rather than assuming the primary dataset's convention.

## 7. Recording soil variables

Extract soil pH, organic matter, texture, and concentration exactly as reported, with units. If a study reports a range or multiple treatment levels, see Section 13.

## 8. Directly reported vs. digitized values

If a number appears explicitly in text or a table, `directly_reported_or_digitized = directly_reported`. If you have to read a value off a bar chart or scatterplot (e.g., using a tool like WebPlotDigitizer), mark `directly_reported_or_digitized = digitized` and name the tool/method in `digitization_method`. Digitized values carry more uncertainty and must never be presented as equivalent in precision to directly reported ones.

## 9. Documenting source location

For every accepted observation, record the exact table number, figure number, or supplementary file name and, where applicable, page number, in `data_source_location`. "Table 3" is not enough if the paper has multiple Table 3-labeled tables across supplementary files; be specific.

## 10. Handling missing information

If a needed field is not reported anywhere in the paper (e.g., no pH reported), leave it blank. Do not impute, estimate from soil type descriptions, or backfill from a regional average. A blank field is honest; a guessed field is not.

## 11. Handling multiple experimental treatments

Many studies report BCF across contamination levels, amendment doses, or cultivars. Extract each as a separate row with a distinct `study_id` suffix (e.g., `10.xxxx_T1`, `10.xxxx_T2`), so no information is collapsed or averaged by you. If you want a single representative value, that is a modeling-time decision, not an extraction-time one.

## 12. Handling replicates

If a paper reports mean ± SD/SE across replicates, extract the mean and record `sample_size` as the number of replicates. Do not extract individual replicate values unless the paper's raw data is provided and you want row-level granularity, in which case treat each replicate as its own row.

## 13. Handling multiple plant components

Extract root, shoot, leaf, whole-plant, etc. as separate rows if the paper reports them separately, matching the primary dataset's `plant_component` granularity where possible.

## 14. Handling multiple elements

Extract each element as its own row.

## 15. Handling transformed or derived BCF values

If BCF is not directly reported but you can compute it from reported plant and soil concentrations using the same numerator/denominator convention as the primary dataset, you may compute it, but explicitly record it as derived: put the computed value in `BCF_value`, keep the source concentrations documented in `notes`, and note "derived by user from reported concentrations, not directly reported" so the provenance is honest. This computation must be done by you from verified source numbers, not inferred or estimated by me.

## 16. Handling incompatible definitions

If, after Section 6, a study's BCF definition cannot be reconciled with the primary dataset's convention (different denominator basis, fresh vs. dry weight with no conversion factor given, etc.), mark `eligibility_status = ineligible` and give a specific `exclusion_reason`. Do not force-fit it.

## 17. Recording uncertainty or ambiguity

Use the `notes` field liberally. If you are 90% sure a value is correct but something about the reporting is unusual, write that down. Future readers of the frozen dataset (including reviewers) benefit from knowing where the soft spots are.

## 18. Verifying every observation before freezing

No row proceeds past `verification_status = unverified` without you personally having inspected the primary source table/figure and completed Sections 3 through 9 for that row. `verified_by_user` should carry your name or initials and the verification date.

## 19. Never guess

If a value cannot be verified from the primary source, leave the field blank and mark the row `requires_manual_verification`. This is worth repeating because it is the single rule most likely to get violated under time pressure: an unverifiable value left blank is more useful to this study than a plausible-looking value that turns out to be wrong.

## 20. Freezing the set

Once all candidate rows have a final `verification_status` of either `verified` or `rejected`, run `overlap_audit_script.py` against the accumulated external CSV and the primary dataset one more time. If it passes cleanly, compute and record a file hash of the frozen CSV (e.g., `sha256sum external_validation_frozen.csv`), timestamp it, and do not edit it again except to append genuinely new, independently verified studies as a documented, re-hashed new version, never a silent edit.
