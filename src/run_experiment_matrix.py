"""Run the pre-specified A–E planning matrix on synthetic data.

The matrix records configurations and status. It intentionally does not
invent empirical results; replace each scenario runner with real inputs only
after the data card and permissions gate is approved.
"""
from __future__ import annotations

import csv
import argparse
from pathlib import Path


SCENARIOS = [
    ("A", "resolution_transfer", "10,20,30 m equivalents", "area error + class F1"),
    ("B", "missing_observations", "cloud/shadow or missing dates", "performance loss + uncertainty"),
    ("C", "label_budget", "25,50,75,100% labels", "learning curve + minimum budget"),
    ("D", "spatial_transfer", "train block != test block", "within-area vs transfer"),
    ("E", "area_robustness", "native vs coarser aggregation", "absolute + relative area error"),
]


def main(output: str = "outputs/experiment_matrix.csv") -> None:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["experiment", "name", "planned_configuration", "primary_outcome", "status"])
        writer.writerows((*row, "PLANNED_SYNTHETIC_SMOKE_TEST") for row in SCENARIOS)
    print(f"Wrote {path} with {len(SCENARIOS)} pre-specified experiments")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="outputs/experiment_matrix.csv")
    args = parser.parse_args()
    main(args.output)
