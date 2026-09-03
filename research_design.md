# Uncertainty-Aware Domain Generalization for Phytoremediation Bioconcentration Prediction
### Research Design Document — v2 (post-audit revisions pending data access)

**Revision log (v1 -> v2), per methodological review:**
1. The spiked-vs-natural/polluted split is no longer assumed valid by definition. Section 2.2 now requires a documented audit (sample counts, BCF distributions, study overlap, confounders) before the split is used for anything. See Section 2.2a.
2. SHAP (Section 3.5) is now computed on a single source-trained model, evaluated separately on held-out source samples vs. shifted-domain samples. A target-trained model is demoted to a supplementary check, gated on sample size.
3. H2 is rewritten as falsifiable: uncertainty is tested for association with error and for OOD-detection utility, not assumed to be higher under shift.
4. `soil_type` is excluded from the model's input features entirely (it only defines the split). OOD/uncertainty experiments now include an error-conditional analysis, not just domain-membership detection.
5. External set target is reframed as quality/diversity-first, not a hard count target.
6. New Section 2.2a: mandatory pre-modeling data-distribution audit.
7. New Section 3.4a: error-vs-uncertainty analysis (binning, monotonicity test, reliability curves, risk-coverage curves) as a named central experiment, not a sub-bullet.
8. Unchanged: modest NN, strong baselines, no architecture-for-its-own-sake.


---

## 1. Research questions and hypotheses

**RQ1 (primary).** Do neural network models trained on spiked-soil bioconcentration data generalize to naturally polluted soils, and can the size of that generalization gap be predicted and flagged at inference time?

**RQ2.** Does explicit uncertainty quantification identify predictions that are unreliable under soil-type domain shift, better than a point-estimate model's residuals alone?

**RQ3.** Which variables drive bioconcentration factor (BCF), and do the drivers differ between spiked and naturally polluted regimes? A driver that matters only under spiked conditions is not actionable for field deployment.

**H1.** Models trained only on spiked-soil data will show significantly degraded performance (higher error, lower calibration) on natural/polluted soil, relative to a spiked-to-spiked held-out test.

**H2.** An epistemic-uncertainty-aware model will assign higher predictive variance to natural/polluted soil inputs than to in-distribution spiked-soil inputs, without being told which regime a sample belongs to at inference time (i.e., the model detects shift from the input features alone, not from a soil-type flag).

**H3.** Feature importance rankings (SHAP) will differ meaningfully between spiked-trained and natural-trained models, specifically for soil pH and element identity, consistent with bioavailability being regime-dependent.

This framing keeps neural networks as the instrument, not the headline. The contribution a reviewer will credit is the domain-shift diagnosis and the decision-relevant uncertainty signal, not "we used a neural net."

---

## 2. Data

### 2.1 Primary dataset
Ha, Sweat, Conrow, Haney, Cahill & LeBauer (2025), *Scientific Data* 12:905. Zenodo DOI 10.5281/zenodo.13363473, CC-BY. Analysis-ready file: `bcfdb.csv` (fields: doi, species, plant_component, element, soil_type, bcf, ph). Raw file `phytoremediation_database.csv` has up to 22 harmonized fields; we will pull additional covariates from the raw file where populated (e.g., pollutant concentration, exposure duration, plant age) rather than relying only on the seven-field slim table, since more covariates give SHAP something real to attribute to.

6,679 BCF observations, 238 studies, 4 species (sunflower, hemp, castor bean, bamboo), 27 elements, `soil_type` in {polluted, spiked, natural, commercial, amended, aqueous, NA}.

### 2.2 Domain-shift split definition (LOCKED, post-audit, v2)
The raw file has 25 fields, not the 7-field slim table originally assumed, and includes two boolean flags (`spiked_soil`, `natural_soil`) independent of the categorical `soil_type` field. Auditing these against `soil_type` found 251 rows labeled `soil_type == "polluted"` that also had `spiked_soil == True`: a hybrid design (field-collected already-polluted soil, further spiked in a pot trial), concentrated in 7 studies. Leaving these in either domain would blur the contamination-history distinction the split exists to capture. Locked protocol:

- **SOURCE (train/val):** `soil_type == "spiked"` → 2,349 rows (post BCF-validity filter), 88 studies. `spiked_soil` is True for 100% of these rows, confirming internal consistency.
- **TARGET (frozen domain-shift test):** `soil_type in {"polluted", "natural", "natural clean"}` AND `spiked_soil == False` → 3,352 rows, 140 studies.
- **EXCLUDED, documented and preserved for supplementary analysis, never discarded** (877 rows): amended soil (472, confounds contamination history with a separate amendment manipulation), hybrid spiked-on-polluted (251), ambiguous rows with missing `spiked_soil` (138), missing `soil_type` (15), commercial substrate (1).
- Within SOURCE, 5-fold grouped cross-validation by `doi`. Verified: zero studies span more than one fold.
- **15 studies contribute rows to both SOURCE and TARGET.** This is a predefined within-study robustness subset (257 rows): the same lab/methodology observed under both conditions, used to check whether the domain effect holds up when between-study noise is controlled for as far as the data allows.
- Only 15 of 204 total studies (~7%) span both domains. Domain is therefore substantially, though not completely, confounded with study source. **The source-to-target difference is treated as a distribution/domain shift finding, not interpreted as a controlled causal domain effect.** This is stated explicitly as a limitation in the manuscript, not implied away.
- External validation (Section 2.3) is frozen separately from this split and touched only once, after model selection is complete on SOURCE/TARGET.
- `soil_type`, `chemical_form`, and `oxidative_state` are never used as model input features. The latter two are near-tautological with domain via missingness pattern (chemical_form: 45.6% missing in source vs. 99.9% in target) and would let a model detect domain rather than learn transferable chemistry.

Full audit trail (exact row counts, per-study/per-element/per-species tables, leakage checks): `pipeline/outputs/`.

### 2.2a Mandatory pre-modeling data-distribution audit
Before any model is trained, the following is computed and reported, and the results determine whether Section 2.2's split proceeds as planned:
- Row counts at each filtering step (raw file -> bcfdb.csv rows -> rows with non-null soil_type -> rows per soil_type category -> final source/target counts).
- BCF distribution (median, IQR, range) per soil_type category, per species, and per element, on the log10 scale, with boxplots.
- Study (`doi`) counts per soil_type category, and the overlap: how many studies contribute to more than one soil_type category (within-study domain pairs are informative; a domain split with zero within-study overlap means "domain" and "study/lab" are perfectly confounded, which is a serious limitation to report honestly rather than hide).
- Species and element coverage per domain: do spiked and natural/polluted subsets cover the same species/element combinations, or does one domain only have data for certain crops or metals? A shift that is actually "different species" dressed up as "different soil condition" would be a mislabeled experiment.
- Feature overlap and covariate shift: compare the distribution of pH, and any other numeric covariates, between domains (KS test or similar).
- Target shift: compare BCF distributions between domains directly, separate from covariate shift, since both can occur together or independently and imply different things about what a model would need to learn.
- Missingness patterns per domain (does natural/polluted data have systematically more missing pH, for instance, which would itself bias comparisons).
- A written judgment, backed by the above numbers, on whether the spiked vs. natural/polluted split constitutes a defensible domain shift for this study, or requires the reclassification protocol described above.

### 2.3 Secondary (external, temporal) validation set
Hand-curated set of BCF observations extracted from papers published after March 2023 (the original dataset's search cutoff) on the same four species, using an identical extraction schema. I will pre-screen and pre-extract candidate rows from open-access sources; you verify against the source PDF before anything enters the frozen test set. Target: 80-150 rows across a minimum of 15 studies, with soil_type recorded per the same taxonomy. This set is frozen: touched exactly once, at the very end, after all model selection and tuning is complete on the primary dataset. I will build the candidate table as a separate deliverable and hand it to you for verification before it is used for anything.

### 2.4 Preprocessing
- BCF is heavily right-skewed (fig2 in the source paper shows a log10-scale plot spanning ~0.005 to several). Model on log10(BCF); report back-transformed metrics too.
- Categorical encoding: species, plant_component, element, soil_type as categorical embeddings for the NN, one-hot for tree baselines.
- Element gets auxiliary numeric features merged in from public periodic-table data: atomic number, ionic radius, electronegativity, atomic mass. This is the mechanistic link Shi et al. found important (ionic radius) and gives the model real chemistry rather than a bare categorical token.
- Missing pH imputed via a missingness indicator + median imputation within species x element, not global mean.
- All preprocessing fit only on the training fold, applied to val/test, to avoid leakage. This is enforced in code via sklearn Pipeline / ColumnTransformer, fit inside the CV loop.

---

## 3. Modeling

### 3.1 Baselines (all with grouped-CV hyperparameter search)
- Linear/ridge regression on log-BCF (sanity floor)
- Random Forest
- Gradient boosted trees (XGBoost or LightGBM)
- These reproduce, on a new dataset, the model class Shi et al. used, giving a fair "does the neural net add anything" comparison rather than a strawman.

### 3.2 Neural architecture
A small feedforward network with entity embeddings for species, plant_component, element, and soil_type, concatenated with numeric features (pH, element physicochemical properties, exposure variables where present). Given ~5,000-6,000 training rows, depth is intentionally shallow: 2-3 hidden layers, dropout, batch norm, early stopping on grouped-validation loss. This is a deliberate choice: a large architecture on a few thousand tabular rows would overfit and would also read as novelty-for-novelty's-sake, which conflicts with your stated design brief.

### 3.3 Uncertainty quantification
`soil_type` is never given to the model as an input feature; it exists only to define the source/target split. Two complementary methods, compared against each other (this comparison is itself a result):
- **Deep ensembles** (5-10 independently initialized networks): captures epistemic uncertainty via prediction variance across the ensemble. Simple, well-validated, no architectural change needed.
- **MC Dropout** at inference time: cheaper, single-model alternative, included so the paper can report whether the more expensive ensemble approach is actually necessary for this problem size, which is a useful negative/positive result either way.
- Calibration assessed via prediction interval coverage probability (PICP) and negative log-likelihood on held-out spiked data, then re-assessed under domain shift on natural/polluted data. The gap between in-domain and shifted calibration is the paper's central diagnostic.

### 3.4 H2, made falsifiable, and OOD detection
H2 is not "uncertainty will be higher under shift." It is two separate, testable claims:
- **H2a:** predictive uncertainty is associated with prediction error (within-domain and under shift), tested via the error-vs-uncertainty analysis in 3.4a. If this fails, the uncertainty estimate is not doing useful work regardless of what happens under shift.
- **H2b:** predictive uncertainty, without access to `soil_type`, has above-chance ability to flag samples as domain-shifted (AUROC of ensemble/MC-dropout variance as a detector of source vs. target membership) and, more practically, above-chance ability to flag samples with large prediction error specifically among target-domain samples (this is the operationally relevant question: not "can it tell domains apart" but "can it tell me not to trust this specific prediction").
- Both are compared against a non-uncertainty baseline OOD detector (Mahalanobis distance or isolation forest on input features) to show any signal is not trivially recoverable from a cheaper method.
- If uncertainty turns out lower or unchanged under shift, that is reported as a finding, not suppressed. A model confidently wrong under distribution shift is itself an important, publishable result and arguably a more interesting one than the "expected" outcome.

### 3.4a Error-vs-uncertainty analysis (central experiment)
- Bin test-set predictions into uncertainty quantiles (e.g., 5-10 bins) and test whether mean absolute error increases monotonically across bins (Spearman correlation between uncertainty and absolute error, plus a formal monotonicity test), computed separately within-domain and under shift.
- Reliability/calibration curves: predicted vs. empirical coverage of nominal prediction intervals (e.g., does the 90% interval actually contain 90% of true values), within-domain and under shift.
- Interval width reported alongside coverage, since wide-but-well-calibrated intervals are less useful than narrow-and-calibrated ones; this trade-off is part of the story.
- Selective prediction / risk-coverage curves: if the model is allowed to abstain on its highest-uncertainty fraction of predictions, how does error on the remaining predictions improve? This is the most decision-relevant framing for a practitioner deciding whether to trust a model's crop recommendation for an unmeasured field site.

### 3.5 Explainability
Primary analysis: SHAP (TreeExplainer for the boosted-tree baseline, DeepExplainer or KernelSHAP for the NN) computed from a single source(spiked)-trained model, evaluated separately on (a) held-out source-domain samples and (b) shifted target-domain samples. Comparing attribution patterns between (a) and (b) directly tests whether the same trained model relies on different features/interactions when scoring shifted inputs, which is a stronger and more defensible claim than comparing two separately trained models. A target-trained model is included only as a supplementary check, and only if the audited target sample size (Section 2.2a) is large enough to support it without overfitting SHAP estimates to noise. This tests H3.

### 3.6 Statistical testing
- Model comparison via 5x2cv paired t-test or corrected resampled t-test (not naive paired t-test on CV folds, which inflates significance) across model classes.
- Domain-shift degradation tested via a permutation test: is the source-to-target performance drop larger than would occur from a random equal-sized split of the source domain alone?
- All effect sizes reported alongside p-values (Cohen's d or equivalent), not p-values alone, per current Q1 statistical-reporting norms.

### 3.7 Ablations
- Remove element physicochemical features -> does performance/SHAP structure degrade, replicating vs. extending Shi et al.'s ionic-radius finding.
- Remove study-grouping in CV -> quantify how much the naive row-level split was overestimating performance, reported as a methodological caution figure.
- Ensemble size sweep (3 vs. 5 vs. 10 members) -> justify the final ensemble size rather than asserting it.
- Deep ensembles vs. MC dropout head-to-head on calibration.

---

## 4. Deliverables I will produce next
1. Environment setup (Python, CUDA for the RTX 5060 Ti, package versions)
2. Data pipeline script: download, clean, merge periodic-table features, build the grouped domain-shift split
3. Baseline training scripts (ridge, RF, XGBoost/LightGBM) with grouped CV and hyperparameter search
4. Neural network + training loop, deep ensemble, MC dropout
5. Evaluation scripts: metrics, calibration, OOD-AUROC, SHAP, statistical tests
6. A single run guide (step by step, what to run in what order, what to send back to me)
7. Candidate external-validation paper list for your verification (separate deliverable, in progress)

Flag anything in this document you want changed before I start writing code, since the code structure follows this document directly.
