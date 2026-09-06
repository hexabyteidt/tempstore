# Verification log — A4: `moso_bamboo_tailings_2023`

## Decision

**Final status: EXCLUDED.** The DOI resolves to a Springer article explicitly labelled **Review**, not a primary experimental study. The accessible primary-source landing page/metadata therefore cannot support extraction of eligible independent BCF observations. The article’s abstract reports transfer coefficients, but no directly reported BCF definition or compatible plant/soil concentration pairs are available on the accessible source. Per protocol, no numerical observation is entered and no transfer coefficient is relabelled as BCF.

## Candidate identity

- **Candidate ID:** `moso_bamboo_tailings_2023`
- **Priority:** A4
- **DOI:** [10.1007/s42729-023-01275-7](https://doi.org/10.1007/s42729-023-01275-7)
- **Title:** *Tolerance and Enrichment Characteristics of Moso Bamboo to Complex Heavy Metal–Contaminated Soil*
- **Authors:** Qi-hang Cai, Yu Zhang, Xue-gang Luo
- **Journal:** *Journal of Soil Science and Plant Nutrition*
- **Volume/pages:** 23:2913–2926 (2023)
- **Publication date:** 12 June 2023; issue date September 2023

## Primary-source evidence inspected

1. **Publisher article page (Springer Nature):** [https://link.springer.com/article/10.1007/s42729-023-01275-7](https://link.springer.com/article/10.1007/s42729-023-01275-7). The article header labels the item **“Review”** and gives the publication date, authors, volume, and pages. The page states that the full article is subscription content and presents “Buy article PDF”; the accessible page is a landing-page/abstract preview rather than the full methods, results tables, or supplements.
2. **Publisher issue listing:** [Volume 23, Issue 3](https://link.springer.com/journal/42729/volumes-and-issues/23-3), item 2. It independently labels the article **“Review”**, lists authors Cai, Zhang, and Luo, gives 12 June 2023 and pages 2913–2926.
3. **Crossref DOI metadata:** [https://api.crossref.org/works/10.1007/s42729-023-01275-7](https://api.crossref.org/works/10.1007/s42729-023-01275-7). Metadata confirms the DOI, title, authors, journal, pages, online publication date 2023-06-12, and a text-and-data-mining license entry; it does not provide the article’s methods/tables or BCF data.
4. **Semantic Scholar record:** [https://www.semanticscholar.org/paper/Tolerance-and-Enrichment-Characteristics-of-Moso-to-Cai-Zhang/34f88d7dcb761f44271fd50734ce44cdb07678b7](https://www.semanticscholar.org/paper/Tolerance-and-Enrichment-Characteristics-of-Moso-to-Cai-Zhang/34f88d7dcb761f44271fd50734ce44cdb07678b7). This is a bibliographic/abstract record pointing back to Springer; it does not supply a primary experimental PDF, tables, or supplements.

## What the accessible primary-source record establishes

### Exact taxon

The publisher abstract explicitly identifies the test material as **Moso bamboo (*Phyllostachys pubescens*)** (Abstract, “Purpose” and “Conclusion”). This is the Phyllostachys/Moso bamboo taxon anticipated by the candidate priority record and is not an ambiguous non-bamboo genus.

### Contamination origin and soil context

The abstract says the study addresses “contaminated soil in tailings areas” (Purpose) and refers to “soil contaminated with heavy metals from the tailings mine” (Conclusion). Thus the accessible abstract supports a tailings/mining-origin contamination description. It does **not**, on the accessible page, provide the mine/location, soil collection coordinates, field-vs-greenhouse setup, amendment history, spiking/dilution details, soil pH/texture/organic matter, or sample collection dates.

### Reported elements and plant comparison

The abstract says above-ground and below-ground enrichment was examined and names **Cr, Mn, Ni, Cu, Zn, and Pb**. It says above-ground content was higher than below-ground roots and gives transfer coefficients of **2.92, 3.06, 1.85, 4.95, 7.48, and 2.44**, respectively, for the treatment groups (publisher abstract, “Results”). These are explicitly described as **transfer coefficients**, not BCFs. Because the full article tables/formula are not accessible and the paper is a review, these values are not extracted as observations.

### Design, treatments, amendments, and duration

The accessible primary-source landing page does not expose the full Materials and Methods or tables. It mentions physiological responses “after remediation” and “different treatments” in the abstract, but does not establish a field or greenhouse design, number of replicates, duration, plant age, control construction, amendments, spiking, dilution, chelation, nutrient solution, or hydroponics. These fields therefore remain unverified/blank rather than inferred.

### BCF definition and values

No BCF formula is available in the accessible publisher abstract/metadata. The abstract reports **transfer coefficients**, not BCF. No directly reported compatible plant concentration and soil concentration pair is available on the accessible source from which a BCF could be calculated. Accordingly:

- **BCF available:** No eligible BCF observations primary-source verified.
- **BCF definition status:** Not reported/verified; do not assume transfer coefficient = BCF.
- **Observations:** Empty array.

## Independence and overlap checks

### DOI-level check against the primary dataset / Ha et al. 2025

The supplied `final_overlap_audit_report.json` lists seven confirmed DOI overlaps and does **not** list `10.1007/s42729-023-01275-7`; its probable-overlap list is empty. The candidate record likewise states `no_exact_doi_match_in_primary_dataset` based on a direct check. Thus there is **no exact DOI overlap** shown in the supplied audit.

That DOI result does not make this review an independent eligible observation study. The accessible article is a review, and the full text is unavailable, so field-site/sample-date overlap or any reuse of Ha et al. material cannot be established from the source. The appropriate conclusion is “not an eligible independent dataset,” not inclusion by DOI absence.

### Relationship to other bamboo / Thurston candidates

The publisher/Crossref record shows that this review cites **Bian et al. 2017, DOI 10.1007/s11356-017-0326-2**, *Phytoremediation potential of Moso bamboo (Phyllostachys pubescens) intercropped with Sedum plumbizincicola in metal-contaminated soil*. That DOI is one of the confirmed-overlap bamboo studies in the supplied audit. The review therefore cannot be counted as a new independent bamboo experiment; it is a secondary synthesis that discusses prior bamboo work. No evidence in the inspected metadata establishes that it shares experimental units with the Thurston/B5 Tar Creek hemp candidates, but this question is moot for eligibility because the candidate is not a primary observation study. No claim of duplicate experimental units is made.

## Eligibility conclusion

The candidate is **EXCLUDED** because the publisher identifies it as a **Review**, contrary to the requirement for primary-source verification of independent BCF observations. The accessible abstract supports the taxon and tailings-origin context, but supplies only transfer-coefficient statements and does not provide a verified BCF definition, compatible numerator/denominator, source location, or treatment/design details. No eligible numerical observations are recorded.

## Source-location notes

- Article identity/type/date: Springer article header; publisher issue listing item 2; Crossref metadata.
- Species and contamination wording: Springer article page, Abstract sections “Purpose” and “Conclusion.”
- Elements and transfer coefficients: Springer article page, Abstract, “Results.”
- Full methods/tables/supplements: unavailable on the accessible publisher preview; page indicates subscription content and paid PDF access.
- Overlap audit: `/home/ubuntu/work/external_curation/final_overlap_audit_report.json`, lines 10–21 (confirmed DOI list and no probable flags); candidate metadata in `/home/ubuntu/work/external_curation/candidate_studies_list.csv`.

**Verification principle applied:** missing or ambiguous values remain missing; transfer coefficients are not relabelled as BCF; no locations, replicates, durations, concentrations, or treatment details are fabricated.
