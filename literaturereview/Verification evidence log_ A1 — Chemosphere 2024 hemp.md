# Verification evidence log: A1 — Chemosphere 2024 hemp

## Final determination

**Final status: `UNRESOLVED`.** The candidate is bibliographically and biologically relevant, and the publisher preview identifies a field experiment in strongly contaminated natural soil. However, the accessible primary-source material does not expose the full methods, tables, figures, or supplement needed to verify the paper's BCF definition, exact BCF values, compatible plant/soil concentration pairs, units, replicates, duration, or observation-level source locations. Under the curation protocol, no numeric BCF observations are admitted when those details cannot be inspected in the primary source.

## Candidate identity

| Field | Verified value | Evidence location |
|---|---|---|
| Study ID | `chemosphere_2024_hemp` | Candidate list; supplied candidate record |
| DOI | `10.1016/j.chemosphere.2024.142199` | ScienceDirect article preview; PubMed record |
| Title | *Industrial hemp (Cannabis sativa L.) can utilize and remediate soil strongly contaminated with Cu, As, Cd, and Pb by phytoattenuation* | ScienceDirect title; PubMed title |
| Authors | Yuan Guo, Lan Wen, Xinlin Zhao, Chen Xing, Rong Huang | ScienceDirect article preview; PubMed citation |
| Journal/date | *Chemosphere*, volume 358, article 142199, June 2024; Epub 29 April 2024 | ScienceDirect lines 19–25; PubMed citation |
| PMID | 38692366 | PubMed record |

The identity is **primary-source verified** at the bibliographic level, but the study is not fully primary-source verified for dataset extraction because the article's complete data-bearing content was not accessible.

## Eligibility checks

### Species and taxa

The article explicitly studies industrial hemp, *Cannabis sativa* L. The abstract states that nine hemp varieties were investigated. This matches the locked target species exactly. The accessible abstract names Z3, Yunma No. 1, Wanma No. 1, and Guangxi Bama in the results, but does not provide the complete nine-variety list.

### Elements

The abstract explicitly identifies Cu, As, Cd, and Pb as the combined contaminants and reports uptake, distribution, and transfer for those elements.

### Contamination origin and soil system

The abstract states that the plants were grown in “strongly contaminated natural soils.” The introduction repeats that the study evaluated the varieties in “natural soils strongly contaminated with Cu, As, Cd, and Pb.” The publisher's indexed section snippet identifies the experimental site as **Tieshan Village, Qibaoshan Town, Liuyang City, Hunan Province, China**, and says that surface soil samples were collected from the experimental site. This is compatible with field-derived/naturally contaminated soil.

The accessible primary-source preview does **not** provide the complete contamination-history methods. It therefore cannot establish from the inspected material whether the field soil was used entirely as collected, whether any soil was spiked, diluted, amended, limed, fertilized, chelated, or otherwise manipulated before planting. The abstract contains no spiking, chelation, hydroponic, nutrient-solution, or exposure-changing-amendment statement, but absence from an abstract is not sufficient to certify the locked exclusion criteria.

### Field versus greenhouse

The publisher preview's “Experimental site and soil physicochemical properties” section begins: “The field experiment was conducted at Tieshan Village, Qibaoshan Town, Liuyang City, Hunan Province, China.” This supports a **field experiment**, not a greenhouse-only or hydroponic experiment. The complete planting layout, plot count, replication, planting date, harvest date, and duration were not accessible.

### BCF definition and values

No BCF formula, BCF table, compatible plant/soil concentration pair, or exact BCF value was available in the accessible publisher preview, PubMed record, or the author-upload status page. The abstract reports percentage retention in roots (Cu 57.7–72.4%; As 47.6–64.7%; Cd 76.0–92.9%; Pb 70.0–87.8%), but these are distribution percentages, **not BCF values**, and were not converted or relabeled as BCF. The abstract also reports biomass and plant-growth measurements, but no soil/plant concentration table from which a compatible BCF can be calculated.

Accordingly, the BCF definition, numerator, denominator, unit basis, plant component, and exact values are **unavailable for primary-source verification**. No observation is included.

## Independence and shared-study assessment

The supplied overlap audit reports no confirmed DOI overlap for this candidate and zero probable-overlap flags. The candidate DOI is not among the seven confirmed overlapping DOIs listed in `/home/ubuntu/work/external_curation/final_overlap_audit_report.json`.

The article was published in 2024, whereas the Ha et al. 2025 dataset was compiled through 15 March 2023 according to the supplied candidate metadata and the Ha dataset description visible on the indexed ResearchGate page. The candidate therefore could not have been one of the studies collected during that stated literature-search cutoff. Its authors and reported site (Guo/Wen/Zhao/Xing/Huang; Tieshan Village, Hunan) do not match the Thurston Tar Creek candidates or the B2 Phyllostachys/Sedum candidate in the supplied candidate list. No evidence was found that this paper reuses the Thurston/B2/B5 experimental units. This supports `independent_from_ha = likely yes` and `shared_experiment_status = no evidence of sharing`, while recognizing that a complete author/methods comparison could not be performed without the full article.

## Structured extraction decision

| Required category | Decision |
|---|---|
| Species | *Cannabis sativa* L. (industrial hemp), nine varieties |
| Elements | Cu, As, Cd, Pb |
| Contamination type | Strongly contaminated natural soil; exact source history beyond the reported field site not fully verified |
| System | Field experiment at Tieshan Village, Qibaoshan Town, Liuyang City, Hunan Province, China |
| Amendments/spiking/dilution | Not established from accessible primary-source content; no eligible observation admitted |
| BCF available | Not verified |
| BCF definition | Unavailable in accessible primary-source content |
| Exact BCF source locations | Unavailable; full tables/figures/supplement could not be inspected |
| Observations | Empty array |

## Source-access caveat

ScienceDirect exposed an article preview containing the title, abstract, introduction excerpts, conclusion, and the opening of the experimental-site section, but required organizational access for the full text. ResearchGate explicitly displayed “No full-text available” and offered only a request-to-author workflow. PubMed provided the authoritative citation and abstract plus an Elsevier full-text link, but not the data tables. Therefore, this verification does not use numerical values from snippets, reviews, or secondary summaries.

## References

[1]: https://www.sciencedirect.com/science/article/abs/pii/S0045653524010920 "ScienceDirect article preview: Industrial hemp (Cannabis sativa L.) can utilize and remediate soil strongly contaminated with Cu, As, Cd, and Pb by phytoattenuation"

[2]: https://pubmed.ncbi.nlm.nih.gov/38692366/ "PubMed record PMID 38692366 for Guo et al. 2024"

[3]: https://www.researchgate.net/publication/380187426_Industrial_hemp_Cannabis_sativa_L_can_utilize_and_remediate_soil_strongly_contaminated_with_Cu_As_Cd_and_Pb_by_Phytoattenuation "ResearchGate record showing no full-text PDF available"

[4]: https://doi.org/10.1016/j.chemosphere.2024.142199 "DOI landing identifier for the candidate study"

[5]: /home/ubuntu/work/external_curation/final_overlap_audit_report.json "Supplied DOI overlap audit"

[6]: /home/ubuntu/work/external_curation/candidate_studies_list.csv "Supplied candidate-study metadata"

[7]: /home/ubuntu/work/external_curation/external_curation_protocol.md "Supplied external curation protocol"

Verified by: Manus subagent, 2026-09-06.

**No eligible BCF observations were primary-source verified; observations are intentionally empty.**
