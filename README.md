# Semantic and Relational Knowledge Preservation — Reproducibility Archive

Public reproducibility package for the study **“Evaluating Semantic and Relational Knowledge Preservation under Fair-Budget Multi-Document Compression.”**

## Scope

This repository contains the validation grid, frozen Run82 selection artifacts, public-safe result tables, and reproducibility notebooks supporting the preservation analyses. It intentionally excludes raw benchmark article text, full generated summaries derived from benchmark articles, private correspondence, and development-only files.

## Frozen Run82 configuration

| Parameter | Value |
|---|---:|
| topic weight (alpha) | 0.30 |
| pattern weight (beta) | 0.70 |
| redundancy penalty (delta) | 1.00 |
| sentence budget | 15 |
| requested topics | 25 |
| historical generation seed | 42 |

Selection was performed only on the validation split using the prespecified lexicographic rule: maximize preservation F1, then ROUGE-2 F1, ROUGE-SU4 recall, compression gain, and finally prefer lower runtime.

The SHA-256 fingerprint of the canonical 120-configuration validation table is:

`9ef9796b30ed6695f501bd330547b8c9b16c00abfe7ad1675d91b99b2a27a29a`

## Repository layout

```text
configs/      frozen selection and run manifests
validation/   complete 120-configuration manifest and scored validation table
notebooks/    validation selection, robustness analyses, and frozen Run82 reproduction
results/      public-safe numeric outputs for PRIMERA, REBEL, WebNLG, ablation, and metric reconciliation
src/          validation-hash verification utility
docs/         data/model acquisition and metric documentation
```

## Reproducibility notebooks

1. `notebooks/00_validation_120_scenarios.ipynb` — reproduces the 120-scenario validation grid and frozen configuration selection. Pareto membership is descriptive only; selection is performed over all valid validation configurations.
2. `notebooks/01_robustness_analysis_master_colab.ipynb` — runs the PRIMERA, REBEL, WebNLG regrouping, and ablation analyses.
3. `notebooks/02_reproduce_frozen_run82.ipynb` — reproduces the frozen Run82 held-out evaluation using the historical seed and frozen configuration.

## Validation hash check

```bash
python src/verify_validation_hash.py
```

Expected SHA-256:

`9ef9796b30ed6695f501bd330547b8c9b16c00abfe7ad1675d91b99b2a27a29a`

## Data and model policy

Raw Multi-News and WebNLG data and pretrained model weights are not redistributed here. Reproduction should obtain those resources from their official sources. Public tables contain identifiers and numeric outputs required to audit the reported analyses without republishing source articles.

## Interpretation boundary

The dependency-based evaluator shows modest component-level gains for Run82 over Lead-W without a reliable exact-triple advantage. The alternative REBEL extractor changes the method ordering, indicating extractor sensitivity. The results therefore support a pipeline-conditional component–structure preservation gap rather than a universal method ranking or universal hierarchy.

## Citation

See `CITATION.cff`.
