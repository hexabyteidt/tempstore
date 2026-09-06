# External Curation Report

## Executive conclusion

The audit began with **12 prioritized candidates**. Primary-source verification supports **4 included studies** contributing **55 observations** from *Cannabis sativa* and *Helianthus annuus*. Three candidates remain **UNRESOLVED**, four are **EXCLUDED**, and one is a confirmed **DUPLICATE_SHARED_STUDY** with the Ha et al. primary dataset. The external dataset is **NOT FROZEN** pending resolution of the unresolved candidates and final confirmation against the complete locked Ha reference corpus.

## Candidate disposition

| Status | Count |
|---|---:|
| Included | 4 |
| Excluded | 4 |
| Duplicate/shared study | 1 |
| Unresolved | 3 |
| Initial prioritized candidates | 12 |

## Included evidence

The included studies are the Slovenia hemp field study, the Kazakhstan sunflower field study, the 0% biochar subset of the Tar Creek hemp greenhouse study, and the Metaleurop Nord hemp phytoattenuation greenhouse study. The studies use compatible plant/soil concentration ratios or explicitly reported BCFs. The B4 values are digitized from primary Figure 2 and retain chart-resolution uncertainty. The A2 values are verifier-derived ratios from directly reported dry-weight plant and soil concentrations.

## Independence and exclusions

B6 was excluded because its DOI and matching observations occur in the Ha et al. primary dataset. B1's 0% biochar controls were retained, while biochar-amended arms were excluded; the related Thurston thesis was not counted as an independent study. B2 remains unresolved because its full methods and possible lineage with a related bamboo study could not be checked. C1 was excluded because clean-soil dilution deliberately changed the exposure regime. A4 was a review rather than a primary experiment. B5 lacked paired field soil denominators, and its greenhouse arm was artificially dosed.

## Dataset composition

The extracted file contains **55 observations** across **4 independent studies**, **2 species**, and **6 elements**. The BCF range is **0.013 to 48.7**, with median **1.06**. There are **20 directly reported observations**, **18 digitized observations**, and **18 verifier-derived observations**.

## Quality gates and limitations

The exact CSV bytes have SHA-256 hash `ad72c4ffe416ae0865aed39cbaef0cddc199ba29bb6260c43d58375e08887ca6`. The file is not declared frozen because three candidates remain unresolved and the complete locked Ha reference files were not supplied locally for a final source-level comparison. Major limitations include study-level clustering, only two represented target species, element imbalance, greenhouse predominance among included observations, heterogeneous soil denominators, digitization uncertainty, missing soil covariates, and potential publication and domain confounding. The data support evaluation of domain shift between experimentally spiked and naturally contaminated or natural observations; they do not support causal claims about soil type.

## References

[1]: https://doi.org/10.1007/s11356-023-30474-z "Flajšman et al. 2023"
[2]: https://doi.org/10.3390/agriculture16131469 "Nugmanov et al. 2026"
[3]: https://doi.org/10.3390/soilsystems8040114 "Thurston et al. 2024"
[4]: https://doi.org/10.1016/j.indcrop.2022.114592 "De Vos et al. 2022"
