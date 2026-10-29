# 16-week implementation roadmap

| Phase | Weeks | Search / verify | Method | Deliverable | Supervisor gate |
|---|---:|---|---|---|---|
| 1. Scope, ethics and charter | 1–2 | Boundary, season, class schema, stakeholder, target journal, local flight and privacy rules | Interview domain owner; write one-page charter; maintain decisions log | Charter, class schema, permissions path | Approve the problem and what the project will not claim |
| 2. Literature and evidence map | 2–4 | Crop mapping, Sentinel-2, UAV, spatial validation, area estimation and reproducibility | Search Scopus/Web of Science/Google Scholar; log query/date/count/exclusions | 25–40-source evidence table + BibTeX/CSV | Reject unsupported or unverifiable sources |
| 3. Data inventory and data card | 3–5 | Sentinel-2 L2A, cloud-quality layers, labels, boundaries, licences and CRSs | Catalogue provider/version/date/resolution/licence/sensitivity/checksum | Data card, scene inventory and licence/privacy register | Approve legal and technical inputs |
| 4. Field and drone protocol | 5–8 | Landowner approval, regulator guidance, weather window, flight and ground-reference protocol | Permission-first pilot route; log actual deviations and QC | Permission file, flight/field log, orthomosaic QC | Approve before any flight or public imagery |
| 5. Baseline, model and A–E experiments | 6–10 | Label manual, features, baseline model, spatial blocks, seed and scenario settings | Run satellite-only first; preserve all planned configurations and weak/null results | Scripts, configs, run manifest, model card, metrics | Approve validation design and claim discipline |
| 6. Validation, paper and release | 10–16 | Held-out metrics, area reference, uncertainty, journal guide, data/code policy, DOI | Clean rerun; report class metrics/intervals; licence/privacy audit | IMRaD draft, figures/tables, data/code statements, archive | Sign off submission and release package |

## Search log minimum fields

`query`, `database`, `date_utc`, `filters`, `retrieved_count`, `screened_count`, `included_count`, `exclusion_reason`, `reviewer`, `export_file`.

## Gate rule

An agent can prepare an artifact, but only the supervisor can approve permissions, change the spatial validation split, authorize a drone flight, approve scientific claims or publish sensitive data.
