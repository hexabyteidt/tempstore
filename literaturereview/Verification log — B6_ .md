# Verification log — B6: `kenya_tannery_bamboo_cr`

## Final decision

**Final status: `DUPLICATE_SHARED_STUDY`.** The candidate is a genuine primary study and its methods and factor table are directly verified. However, it is not independent from Ha et al. (2025): the exact DOI, `10.5696/2156-9614-7.16.12`, is already present in the Ha open dataset (`raw_data/phytoremediation_database.csv` and `data/bcfdb.csv`). The supplied overlap audit’s confirmed-DOI list was incomplete for this unconfirmed candidate, so the downloaded Ha source was checked directly rather than relying only on that audit.

No observations are returned in the structured result because this study cannot be added as an independent external observation set after exact DOI matching to Ha et al. The primary source nevertheless directly verifies the study’s BCF definition and values, documented below for auditability.

## Candidate identity and primary sources

- **Candidate ID:** `kenya_tannery_bamboo_cr`
- **Priority:** B6
- **Candidate title:** *Phytoremediation Using Bamboo to Reduce the Risk of Chromium Exposure from a Contaminated Tannery Site in Kenya*
- **Verified citation:** Were FH, Wafula GA, Wairungu S. *Phytoremediation Using Bamboo to Reduce the Risk of Chromium Exposure from a Contaminated Tannery Site in Kenya.* **Journal of Health & Pollution.** 2017;7(16):12–25. Published 18 December 2017. DOI: `10.5696/2156-9614-7.16.12`. PMID 30524836; PMCID PMC6221446.
- **Primary full text:** [PMC6221446](https://pmc.ncbi.nlm.nih.gov/articles/PMC6221446/)
- **Publisher/DOI full text:** [https://doi.org/10.5696/2156-9614-7.16.12](https://doi.org/10.5696/2156-9614-7.16.12)
- **Primary-source status:** Verified from the NCBI/PMC full article and its structured table XML; PubMed independently confirms the citation and DOI.

## Exact species/taxa

The Methods section, “Sampling of Bamboo Rooted Cuttings,” identifies six taxa: *Bambusa blumeana*, *Bambusa bambos*, *Bambusa vulgaris*, *Dendrocalamus asper*, *Dendrocalamus birmanicus*, and *Dendrocalamus membranaceus* (PMC full text, Methods; article HTML around the rooted-cuttings section). The BCF table names the same six species (Table 6, “Accumulation and Translocation of Chromium in Six Different Bamboo Species in the Tannery and Control Site”).

The locked primary-dataset terminology is the coarse species category **Bamboo**. The Ha database contains the exact DOI and records *Bambusa vulgaris* from this paper under `species = Bamboo`, `variety = Bambusa vulgaris`; it does not establish that the five other taxa from the paper were independently extracted into the frozen data. Accordingly, the taxonomic scope is not the reason for rejection: exact-study duplication is.

## Contamination origin and design

The study is field-derived and naturally contaminated. The Site Description states that the study area was a chromium-contaminated acre within a selected tannery at **1°17′0″ South, 36°42′0″ East**, with land-based tannery-waste disposal since 1994. The article attributes contamination to chrome-sulphate spillage, unused chrome discharged in effluent, chromium-containing sludge dumped in the open field, chromium-bearing leather waste/shavings/dust, and burning/dumping practices (Methods, Site Description and Table 1, “Description of Major Activities in the Tannery Associated with Chromium Contamination”). Tannery soil Cr was 1337.0–3398.0 mg/kg dry weight; control-garden soil was 0.20–2.34 mg/kg dry weight (Abstract; Table 2).

The design was not a greenhouse or hydroponic experiment. Eighty-four three-month-old rooted cuttings were initially nurtured in black polythene pots with Cr-free soil at the Kenya Forestry Research Institute, then transplanted to **72 holes at the tannery** and **12 holes in a garden control site**. Holes were approximately 60 cm diameter and 30 cm depth and spaced 2 m apart. Each hole was refilled with its corresponding collected soil; plants were then rain-fed and maintained in a natural environment (Methods, “Sampling of Soils and Transplanting of Bamboo Rooted Cuttings”). The study began January 2015 and ended January 2017; growth and tissue sampling were after two years (Methods, opening paragraph and “Growth Performance and Chromium Levels”).

No experimental spiking, dilution with clean soil, chelation, nutrient solution, hydroponics, or primarily exposure-changing amendment is described. The initial Cr-free nursery soil was used only to nurture rooted cuttings before field transplanting; the measured exposure phase used the existing tannery soil. The control was a separate garden soil site, not an imposed dilution treatment.

## BCF definition and directly verified values

The Methods subsection “Accumulation and Translocation of Chromium” defines:

> “The BCF was defined as the ratio of Cr levels in the roots to that of the rhizosphere soil of the bamboo species.”

The same subsection defines TF as shoot Cr/root Cr and BAF as shoot Cr/rhizosphere-soil Cr. Thus the paper’s compatible BCF numerator is **root total-Cr concentration** and denominator is **corresponding rhizosphere-soil total-Cr concentration**. Plant and soil concentrations were measured as total Cr by ICP-OES and expressed in **mg/kg dry weight** (Methods, “Analysis of Total Chromium Levels”).

Table 6 directly reports the following mean ± SE factors for the tannery and control sites. These are recorded here only to document primary-source verification; they are not emitted as independent observations because the exact DOI is already in Ha et al.:

| Site | Taxon | TF | BCF (root/rhizosphere soil) | BAF (shoot/rhizosphere soil) |
|---|---|---:|---:|---:|
| Tannery | *Bambusa blumeana* | 0.24 ± 0.05 | 1.13 ± 0.02 | 0.27 ± 0.05 |
| Tannery | *Bambusa bambos* | 1.10 ± 0.05 | 0.49 ± 0.07 | 0.53 ± 0.07 |
| Tannery | *Bambusa vulgaris* | 0.02 ± 0.01 | 1.53 ± 0.11 | 0.03 ± 0.01 |
| Tannery | *Dendrocalamus asper* | 0.09 ± 0.01 | 1.64 ± 0.10 | 0.14 ± 0.02 |
| Tannery | *Dendrocalamus birmanicus* | 0.21 ± 0.03 | 0.79 ± 0.05 | 0.16 ± 0.02 |
| Tannery | *Dendrocalamus membranaceus* | 0.07 ± 0.01 | 1.34 ± 0.09 | 0.10 ± 0.02 |
| Control | *Bambusa blumeana* | 3.19 ± 1.16 | 0.84 ± 0.68 | 1.90 ± 1.19 |
| Control | *Bambusa bambos* | 2.54 ± 1.72 | 0.31 ± 0.19 | 0.48 ± 0.07 |
| Control | *Bambusa vulgaris* | 0.22 ± 0.03 | 0.83 ± 0.24 | 0.18 ± 0.03 |
| Control | *Dendrocalamus asper* | 0.80 ± 0.43 | 2.57 ± 0.43 | 1.47 ± 0.07 |
| Control | *Dendrocalamus birmanicus* | 0.16 ± 0.08 | 2.21 ± 0.03 | 1.83 ± 0.79 |
| Control | *Dendrocalamus membranaceus* | 3.07 ± 0.24 | 0.78 ± 0.04 | 2.41 ± 0.31 |

**Exact location:** primary article Table 6, caption “Accumulation and Translocation of Chromium in Six Different Bamboo Species in the Tannery and Control Site.” The table is available as the article’s structured PMC table asset `i2156-9614-7-16-12-t06.xml`; the article pagination is 12–25. The formula is in Methods, subsection “Accumulation and Translocation of Chromium.” Table 2 reports the pre-transplantation soil concentrations and physicochemical variables; Table 4 reports two-year rhizosphere-soil, root, and shoot Cr concentrations as an image/table asset. No digitization was used.

The primary article reports triplicate analytical determinations as mean ± SE (Methods, “Statistical Analysis” and “Quality Assurance and Control”). Table 2 states that two of the 12 *D. birmanicus* tannery samples failed to grow to maturity; this is why the tannery soil summary is N=70 rather than 72 for that comparison. The paper does not provide a single uniform per-species sample-size statement in Table 6 beyond the field-hole design; therefore no sample size is assigned to any independent observation here.

## Ha et al. (2025) exact-overlap check

The Ha et al. open dataset was downloaded from [Zenodo record 10.5281/zenodo.13363473](https://zenodo.org/records/13363473). Direct search of both `raw_data/phytoremediation_database.csv` and `data/bcfdb.csv` found the exact DOI `10.5696/2156-9614-7.16.12`. The Ha rows include:

- `Bamboo`, DOI `10.5696/2156-9614-7.16.12`, variety `Bambusa vulgaris`, location `1° 17' 0" S, 36° 42' 0" E`, date `2015-01~2017-01`, treatment `Tannery`, Cr, soil concentration 2107.4 mg/kg, BCF 1.53, plant component `Root`, natural soil TRUE, soil pH 7.99, organic matter 3.43, soil type `polluted`.
- The same dataset also records the corresponding *B. vulgaris* control root row (soil concentration 0.44 mg/kg, BCF 0.83) and stem rows (tannery BCF 0.03; control BCF 0.18).

The exact DOI match is conclusive for duplicate/shared-study status. It supersedes the supplied overlap-audit report’s statement that only seven other confirmed DOI overlaps were present; that audit did not include this candidate DOI because the candidate list still marked it unconfirmed.

## Relationship to other candidates

No evidence of shared experimental units with the Thurston Tar Creek hemp candidates B1/B5 was found: the Kenya paper has different authors, institutions, country, tannery site, species, element, DOI, and field dates. It is also distinct in bibliographic identity and field site from B2 (*Phyllostachys praecox* 2018) and from the other Chinese bamboo studies. Those distinctions do not restore eligibility because the Kenya study is already incorporated in Ha et al. through the exact DOI.

## Structured extraction conclusion

- **BCF available:** Yes, directly reported in Table 6.
- **BCF definition status:** Compatible and explicit for root/rhizosphere soil; BAF is separately defined as shoot/rhizosphere soil and must not be relabelled as BCF.
- **Eligible independent observations:** None, because the exact DOI is already in Ha et al. 2025.
- **Observations array for the external set:** Empty.
- **Reason:** Primary-source verified study, but exact DOI/shared-study duplication with Ha et al.; do not count again.

## Sources inspected

1. NCBI/PMC full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC6221446/
2. PubMed record: https://pubmed.ncbi.nlm.nih.gov/30524836/
3. DOI/publisher rendering: https://doi.org/10.5696/2156-9614-7.16.12
4. Ha et al. article: https://www.nature.com/articles/s41597-025-05239-7
5. Ha et al. open data and code: https://zenodo.org/records/13363473
6. Supplied overlap audit: `/home/ubuntu/work/external_curation/final_overlap_audit_report.json`

No numerical values were inferred from snippets, reviews, plots, or AI summaries. Values cited above are from the primary article’s methods/tables or the directly downloaded Ha dataset.
