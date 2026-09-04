# TARGET `natural clean` Sensitivity Analysis

## 1. What the data actually shows

`natural clean` is not documented in Ha et al.'s published metadata beyond the bare category label, so its meaning is determined here empirically from the harmonized rows themselves, not assumed from the name.

After the locked filtering protocol (source/target classification, invalid-BCF removal), `natural clean` contributes **41 rows from exactly 3 studies**, all of them **Hemp**, covering **Pb (14), Zn (14), Cd (12), Ni (1)**. DOIs: `10.1007/s11356-023-25198-z`, `10.1007/s41742-022-00446-1`, `10.1023/a:1026113905129`.

Compared against the rest of TARGET (`polluted` + `natural`, 3,311 rows):

| Metric | natural clean | rest of TARGET |
|---|---|---|
| soil_concentration, median | 81.0 | 120.0 |
| soil_concentration, 25th pct | 1.3 | 23.7 |
| soil_concentration, max | 259 | 119,645 |
| log10(BCF), median | -1.54 | -0.57 |
| log10(BCF), mean | -1.40 | -0.70 |

KS test on log-BCF: statistic 0.377, p = 1.1e-05. Cohen's d = -0.87 (large effect). KS test on soil_concentration: statistic 0.362, p = 3.1e-05. Both distributions differ sharply, and in the direction implied by the label: `natural clean` sits at markedly lower soil concentration (25th percentile 1.3 vs. 23.7, roughly an order of magnitude, and a maximum of 259 versus 119,645 for the rest of TARGET) and markedly lower BCF.

**Interpretation:** the data is consistent with `natural clean` representing low-background or genuinely uncontaminated field soil, most plausibly used as a paired control plot alongside a polluted plot within the same three hemp studies. This is a defensible reading of the numbers, not a claim about study design that the raw file confirms directly, since no field in the schema states "this is a control." That distinction matters and is carried into the recommendation below.

## 2. Should it be grouped with `polluted`/`natural`?

As currently defined, TARGET already includes it (per the locked protocol: `soil_type in {polluted, natural, natural clean}` AND `spiked_soil == False`). The case for leaving it in: it is genuinely non-spiked, field-grown soil, which is the defining property of TARGET. The case for concern: it is drawn from only 3 studies, all one species, and looks compositionally more like a background/negative-control regime than a "contaminated field site" regime, the scenario the domain-shift experiment is actually trying to characterize (does a model trained on artificially spiked soil generalize to real contaminated land). Mixing a low-concentration control regime into TARGET risks diluting the target-domain BCF distribution toward values that don't represent the deployment scenario of interest, and risks the 41-row, 3-study, single-species subset having outsized leverage on any within-TARGET summary statistic given its distinctiveness.

**Recommendation: do not modify the locked TARGET partition now**, per your instruction. Instead, treat this as a named, predefined robustness question, answered after model training via the sensitivity analysis below, not by silently redefining TARGET.

## 3. Predefined sensitivity analysis (to run once test-set evaluation begins, not before)

Three comparisons, planned now and executed unmodified later:

**3a. TARGET-full vs. TARGET-minus-natural-clean.** Recompute every headline TARGET metric (calibration, error, uncertainty-error association, OOD-AUROC) with the 41 `natural clean` rows excluded, and report both numbers side by side. If results are materially unchanged, the category isn't driving the finding and this becomes a one-line footnote. If results shift meaningfully, that is itself reported, not hidden.

**3b. `natural clean` in isolation vs. `polluted`+`natural` in isolation.** Evaluate the trained model's error and uncertainty separately on the 41 `natural clean` rows and on the remaining 3,311 rows. This is a descriptive comparison of two subpopulations within TARGET, not a hypothesis test with a preregistered significance threshold, since n=41 from 3 studies of 1 species is too thin to support a strong inferential claim.

**3c. Directional consistency check.** If the model's error is systematically different (better or worse) on `natural clean` than on the rest of TARGET, report this as evidence about what kind of "natural" scenario the model handles well or poorly, e.g. "the model's target-domain error is concentrated in genuinely contaminated field soil rather than background-level soil" or the reverse. This is reported as a descriptive pattern, not a causal claim about why, since the same species/study confound documented in the main design doc applies here at an even smaller scale.

## 4. Interpretation guardrails

None of this analysis supports a causal claim that "background soil differs from polluted soil in bioavailability by X amount," because domain (here, sub-domain) is confounded with study and species at n=3 studies, 1 species. It supports only the narrower, honest claim: within this dataset, the `natural clean`-labeled rows are numerically distinct from the rest of TARGET, and the model's behavior on them is reported separately so a reader can judge whether the 41 rows are pulling the headline TARGET result in a particular direction.
