"""Synthetic, spatially separated AgriMap baseline.

This is deliberately a small smoke test. It demonstrates the reporting shape
without pretending that synthetic pixels are field observations.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


CLASS_NAMES = np.array(["crop_a", "crop_b", "soil", "water"])


def make_synthetic_grid(size: int, seed: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:size, 0:size]
    zone = np.zeros((size, size), dtype=int)
    zone[(xx > size * 0.48) & (yy < size * 0.42)] = 1
    zone[(yy > size * 0.58) & (xx < size * 0.57)] = 2
    zone[(xx > size * 0.68) & (yy > size * 0.65)] = 3
    base = np.array([[0.13, 0.25, 0.10, 0.62], [0.10, 0.34, 0.13, 0.56], [0.35, 0.28, 0.25, 0.18], [0.22, 0.30, 0.36, 0.08]])
    features = base[zone] + rng.normal(0, 0.025, (size, size, 4))
    # Make edges imperfect so the smoke test has a meaningful confusion matrix.
    features += (np.sin(xx / 7.0) + np.cos(yy / 9.0))[..., None] * 0.006
    return features.clip(0, 1), zone, np.stack([xx, yy], axis=-1)


def spatial_split(coords: np.ndarray, train_fraction: float, test_fraction: float) -> tuple[np.ndarray, np.ndarray]:
    block = (coords[..., 0] // max(1, coords[..., 0].max() // 4 + 1)) + 2 * (coords[..., 1] // max(1, coords[..., 1].max() // 4 + 1))
    train = block == 0
    test = block == 3
    if train.sum() == 0 or test.sum() == 0:
        raise ValueError("Synthetic spatial split produced an empty train/test block")
    return train.ravel(), test.ravel()


def run(seed: int = 42, grid_size: int = 80, output_dir: str = "outputs/baseline") -> dict:
    features, labels, coords = make_synthetic_grid(grid_size, seed)
    train_mask, test_mask = spatial_split(coords, 0.60, 0.20)
    x = features.reshape(-1, features.shape[-1])
    y = labels.ravel()
    model = RandomForestClassifier(n_estimators=120, random_state=seed, n_jobs=-1, class_weight="balanced")
    model.fit(x[train_mask], y[train_mask])
    predicted = model.predict(x[test_mask])
    matrix = confusion_matrix(y[test_mask], predicted, labels=np.arange(len(CLASS_NAMES)))
    metrics = {
        "synthetic_demo": True,
        "seed": seed,
        "grid_size": grid_size,
        "spatial_train_pixels": int(train_mask.sum()),
        "spatial_test_pixels": int(test_mask.sum()),
        "overall_accuracy": float(accuracy_score(y[test_mask], predicted)),
        "macro_f1": float(f1_score(y[test_mask], predicted, average="macro", zero_division=0)),
        "classes": CLASS_NAMES.tolist(),
        "warning": "Do not interpret synthetic demo metrics as field performance.",
    }
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    pd.DataFrame(matrix, index=CLASS_NAMES, columns=CLASS_NAMES).to_csv(out / "confusion_matrix.csv")
    area = pd.Series(y).value_counts().sort_index().reindex(range(len(CLASS_NAMES)), fill_value=0)
    pd.DataFrame({"class": CLASS_NAMES, "mapped_pixels": area.values}).to_csv(out / "class_area.csv", index=False)
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="baseline", choices=["baseline"])
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--grid-size", type=int, default=80)
    parser.add_argument("--output-dir", default="outputs/baseline")
    args = parser.parse_args()
    print(json.dumps(run(args.seed, args.grid_size, args.output_dir), indent=2))
