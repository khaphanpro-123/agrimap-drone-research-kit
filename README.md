# AgriMap Drone Research Kit

An open, reproducible starter for the AgriMap Drone research plan: crop-type mapping and agricultural field-area estimation from an open satellite baseline, with drone imagery treated as a measured comparison layer.

> The demo uses synthetic data. It is a pipeline smoke test and an experiment-design example, not evidence about a real farm.

## What is included

- `src/run_demo.py` — spatially separated Random Forest baseline on a synthetic multi-band grid.
- `src/run_experiment_matrix.py` — pre-specified A–E robustness matrix (resolution, missing observations, label budget, spatial transfer, area robustness).
- `configs/baseline.yaml` — one human-readable configuration with fixed seed and output paths.
- `prompts/agent-prompts.md` — bounded prompts for research librarian, data steward, UAV planner, ML engineer and reproducibility reviewer agents.
- `docs/research-roadmap.md` — 16-week phase plan, search tasks, artifacts and supervisor gates.
- `.github/workflows/validate.yml` — a small CI smoke test for the demo.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python src/run_demo.py --scenario baseline
python src/run_experiment_matrix.py
```

Outputs are written to `outputs/` (metrics JSON, area CSV, confusion matrix CSV and an optional map PNG). The scripts never download private imagery and never infer permissions.

## Research guardrails

1. Replace synthetic data only after the study area, class schema, licences and land-access permissions are documented.
2. Keep spatially separated train/tuning/test blocks; random pixel splits are not an acceptable final validation design.
3. Run the satellite-only baseline before adding drone imagery.
4. Report class-wise metrics, area error and uncertainty intervals; do not report a single accuracy number as the complete result.
5. Treat an anomaly or stress flag as a location for inspection, never as a diagnosis of disease, water shortage or yield.

## Reproducibility

The configuration, random seed, source version and run manifest are part of every output directory. Before submission, archive a tagged release and persistent DOI, add a data card, and remove or protect sensitive raw boundaries and imagery.

## Linked briefing

The interactive supervisor briefing is published at:
https://agrimap-drone-supervisor-20261029.phanvankha06122004.chatgpt.site
