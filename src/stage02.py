"""Stage 02 — basic exploratory data analysis (CSV tables and PNG figures)."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "assets" / "tables_eda"
FIGURES = ROOT / "assets" / "figures_eda"


def save_plot(name: str) -> None:
    plt.tight_layout()
    plt.savefig(FIGURES / name, dpi=170, bbox_inches="tight")
    plt.close()


def run(dataset: Path = ROOT / "assets" / "dataset.csv") -> None:
    """Read stage01 CSV or a legacy Excel workbook, without touching source files."""
    for directory in (TABLES, FIGURES):
        if not directory.is_dir():
            raise FileNotFoundError(f"Provision the output directory first: {directory}")
    if dataset.suffix.lower() in (".xlsx", ".xls"):
        df = pd.read_excel(dataset, sheet_name=0, dtype={"id": str})
    else:
        df = pd.read_csv(dataset, dtype={"id": str})
    numerical = df.select_dtypes(include="number")
    if numerical.empty:
        raise ValueError("The input contains no numerical features.")

    overview = pd.DataFrame({
        "metric": ["records", "columns", "numeric_columns", "duplicate_rows"],
        "value": [len(df), len(df.columns), len(numerical.columns), int(df.duplicated().sum())],
    })
    overview.to_csv(TABLES / "overview.csv", index=False)
    df.isna().sum().rename("missing_count").rename_axis("feature").to_csv(
        TABLES / "missing_values.csv"
    )
    numerical.describe().transpose().rename_axis("feature").to_csv(
        TABLES / "descriptive_statistics.csv"
    )
    correlations = numerical.corr(numeric_only=True)
    correlations.to_csv(TABLES / "correlations.csv")

    for name in ("State", "ClusterName"):
        if name in df.columns:
            counts = df[name].value_counts(dropna=False).rename_axis(name).reset_index(name="count")
            counts.to_csv(TABLES / f"counts_{name.lower()}.csv", index=False)
            plt.figure(figsize=(12, 4.5))
            sns.barplot(data=counts, x=name, y="count")
            plt.title(f"Distribution by {name}")
            plt.xticks(rotation=45)
            save_plot(f"counts_{name.lower()}.png")

    if len(correlations) > 1:
        plt.figure(figsize=(16, 13))
        sns.heatmap(correlations, vmin=-1, vmax=1, center=0, cmap="coolwarm",
                    xticklabels=True, yticklabels=True)
        plt.tick_params(labelsize=5.5)
        plt.title("Pearson correlation matrix — numeric columns")
        save_plot("correlations.png")

    # Each numeric variable has its own PNG to retain readable axes and scales.
    for name in numerical:
        values = numerical[name].replace([np.inf, -np.inf], np.nan).dropna()
        if values.empty:
            continue
        plt.figure(figsize=(7.5, 4.2))
        sns.histplot(values, bins=35)
        plt.title(f"Distribution: {name}")
        plt.xlabel(name)
        identifier = re.sub(r"[^A-Za-z0-9_-]+", "_", str(name))
        save_plot(f"hist_{identifier}.png")
    print(f"stage02: CSV tables -> {TABLES}; PNG figures -> {FIGURES}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "assets" / "dataset.csv")
    args = parser.parse_args()
    run(args.input)


if __name__ == "__main__":
    main()
