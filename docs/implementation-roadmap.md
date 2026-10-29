# Implementation Roadmap: from a research question to an auditable article

The sequence below deliberately places **scope, permission and evidence planning before modelling**. Do not begin a drone flight or train a model because an agent has suggested it; proceed only when the acceptance criterion for the preceding stage is met.

| Stage | Weeks | Need to find | How to search / collect | Deliverable & acceptance criterion |
|---|---:|---|---|---|
| 0. Scope & governance | 1–2 | Study boundary; crop/land-cover class schema; season; owner/authority contacts; target journal shortlist | Meet domain stakeholders; create a one-page study charter; review local flight, privacy and land-access rules | Signed/approved charter, class definitions, data-management plan, permission path. No modelling before this is stable. |
| 1. Literature & evidence map | 2–4 | Recent peer-reviewed crop mapping, UAV, spatial validation and area-estimation papers; foundational method papers | Search Scopus/Web of Science/Google Scholar with a dated search log. Combine `crop type mapping`, `Sentinel-2`, `(UAV OR drone)`, `spatial cross-validation`, `area estimation`, target crop/country; screen titles → abstracts → full text | CSV/BibTeX search log, 25–40 relevant sources, claim-to-source matrix. Every planned claim has direct support. |
| 2. Data inventory | 3–5 | Sentinel-2 L2A scenes, cloud/quality documentation, field boundaries, reference labels, licences | Catalogue exact product/version/date/resolution/licence/access URL. Inspect cloud cover and phenological dates; record unavailable data too | Data card, scene inventory, licence register, privacy assessment, initial geospatial folder structure. |
| 3. Field & drone protocol | 5–8 | Permission, weather window, flight plan, GSD, overlap, sensor configuration, ground-reference protocol | Use regulator/authority rules for the actual country; coordinate landowner; pilot a small route; log every change from plan | Permission record, safety assessment, flight/field log, image metadata, orthomosaic QC report. |
| 4. Baseline & simulations | 6–10 | Label manual, features, transparent baseline, comparison model, A–E configurations | Write configurations before looking at final test metrics. Start with satellite-only baseline; fix spatial blocks; version random seeds | Reproducible scripts, run manifest, A–E result matrix including weak/null results, model card. |
| 5. Validation & area | 10–12 | Spatial hold-out metrics, class-wise errors, uncertainty method, independent area reference | Never random-split adjacent pixels. Test in held-out blocks/farms. Bootstrap or otherwise document intervals. Compare reference and mapped area | Error matrix, class metrics, area table, uncertainty statement, limitation register. |
| 6. Paper & open release | 12–16 | Chosen journal author guide, data policy, code policy, repository DOI options | Map every figure/table to a script; have an independent person rerun README from a clean environment; archive non-sensitive code/data | IMRaD manuscript, figure/table package, data & code statements, DOI/release record, submission checklist. |

## Search protocol template

1. Record platform, date, full query, filters, number retrieved and export format.
2. Deduplicate in Zotero/Mendeley; keep the `.bib` export and exclusion reasons.
3. Screen with predefined inclusion rules: peer-reviewed; crop/land mapping; method/data relevant to this landscape; readable methodology; licence/availability where needed.
4. Extract **method, data product, spatial validation protocol, metrics, limitation and DOI**, not just a conclusion.
5. Use sources only where they support the exact manuscript sentence or configuration.

## Human review gates

- **Gate A (before drone work):** supervisor confirms scope, safety/permission and privacy plan.
- **Gate B (before final model):** supervisor reviews class definitions, spatial split and simulation configuration.
- **Gate C (before public release):** supervisor reviews claims, licences, sensitive boundary treatment and reproducibility test.
