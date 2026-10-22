"""Reprodução executável de notebooks/cluster_analysis.ipynb.

Fontes: as abas ProbFeatures, state e dummy de data/deparas.xlsx.
Saídas: CSV em assets/tables_thesis, PNG em assets/figures_thesis,
e dataset completo em assets/cluster_analysis_dataset.csv.

Preserva as 51 variáveis, a geração por perfil, MinMaxScaler, KMeans com
init='random', seis clusters e as análises do notebook. Pequenas adaptações
são necessárias para executar fora do Jupyter (salvar figuras e numeric_only).
O notebook não registra seed para a geração sintética; --seed 42 torna a
nova execução reprodutível sem alegar igualdade com a amostra histórica.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
TABLES = ASSETS / "tables_thesis"
FIGURES = ASSETS / "figures_thesis"
COUNTS = (("c1", 2500), ("c2", 800), ("c3", 700),
          ("c4", 400), ("c5", 300), ("c6", 500))
EXCLUDED = ("id", "ClusterName", "IdBranch", "State",
            "DummyInsideShopping", "DummyPrimeZone")
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 4))


def read_parameters(workbook: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return (
        pd.read_excel(workbook, sheet_name="ProbFeatures"),
        pd.read_excel(workbook, sheet_name="state"),
        pd.read_excel(workbook, sheet_name="dummy"),
    )


def create_cluster(dp: pd.DataFrame, cluster: str, dpuf: pd.DataFrame,
                   dpdummy: pd.DataFrame, n: int) -> pd.DataFrame:
    """Port of CreateCluster; preserve reverse feature order and RNG call order."""
    parameters = dp[dp["ClusterName"] == cluster]
    names = list(parameters.Features)
    means = list(parameters.Mean)
    deviations = list(parameters.Std)
    m = len(names)
    if m != 51:
        raise ValueError(f"{cluster}: expected 51 features; got {m}")
    df = pd.DataFrame({"id": np.arange(1, n + 1)})
    df["id"] = df["id"].astype(int).apply(lambda x: "{0:0>4}".format(x)).astype(str)
    df["ClusterName"] = parameters["ClusterName"].unique()[0]
    df["IdBranch"] = df["ClusterName"] + "_" + df["id"]
    for k in range(m):
        i = m - k - 1
        values = np.round(np.random.normal(means[i], deviations[i], n), 0).astype(int)
        df = df.join(pd.DataFrame({names[i]: values}))
    for feature in ("NumberManagerBusinessCapacity",
                    "NumberManagerPersonalCapacity", "NumberTellerCapacity"):
        df.loc[df[feature] <= 0, feature] = 1
    df["State"] = random.choices(
        population=list(dpuf.State.unique()),
        weights=list(dpuf.Apriori.unique()),
        k=n,
    )
    for feature in ("DummyInsideShopping", "DummyPrimeZone"):
        p = dpdummy[
            (dpdummy["ClusterName"] == cluster) & (dpdummy["Features"] == feature)
        ]["Probability"].values[0]
        df[feature] = random.choices(population=[1, 0], weights=[p, 1-p], k=n)
    return df


def generate_dataset(dp: pd.DataFrame, dpuf: pd.DataFrame,
                     dpdummy: pd.DataFrame) -> pd.DataFrame:
    frames = [create_cluster(dp, name, dpuf, dpdummy, n) for name, n in COUNTS]
    return pd.concat(frames).reset_index().drop(columns="index")


def creating_clusters(df: pd.DataFrame, dfx: pd.DataFrame, n: int = 6):
    """Exact KMeans configuration and MinMax preprocessing from the notebook."""
    x = dfx
    x_scaled = MinMaxScaler().fit_transform(x)
    kmeans = KMeans(init="random", n_clusters=n, n_init=10, max_iter=300,
                    random_state=42).fit(x_scaled)
    clusters = pd.DataFrame(kmeans.labels_, columns=["Cluster"]).astype(int)
    return df.join(clusters), x, np.array(x), clusters, kmeans


def creates_cluster_pivot_table(df: pd.DataFrame) -> pd.DataFrame:
    pt = pd.pivot_table(
        df, values="IdBranch", index="ClusterName", columns="Cluster",
        fill_value=0, aggfunc="count",
    ).reset_index()
    return pt.rename(columns={i: f"C{i+1}" for i in range(6)})


def creates_dispersion_table(df: pd.DataFrame, dp: pd.DataFrame) -> pd.DataFrame:
    """Original std/mean per variable and cluster, adapted for pandas >=2."""
    averages = df.groupby("Cluster").mean(numeric_only=True).T
    deviations = df.groupby("Cluster").std(numeric_only=True).T
    cluster_ids = sorted(df["Cluster"].unique())
    means = averages.rename(columns={i: f"C{i+1}Mean" for i in cluster_ids})
    stds = deviations.rename(columns={i: f"C{i+1}Std" for i in cluster_ids})
    table = means.join(stds)
    for i in cluster_ids:
        table[f"C{i+1}Disp"] = table[f"C{i+1}Std"] / table[f"C{i+1}Mean"]
    table.index.name = "Features"
    meta = dp[["FeatureGrouping", "Features"]].drop_duplicates()
    return pd.merge(meta, table.reset_index(), how="left", on="Features")


def save_figure(name: str, *, dpi: int = 100) -> None:
    plt.savefig(FIGURES / name, dpi=dpi, bbox_inches="tight")
    plt.close()


def export_elbow(x: pd.DataFrame, *, seed: int) -> None:
    # The original elbow method uses RAW (unscaled) x; KMeans uses scaled x.
    # Fix the previously unspecified elbow seed to make this output reproducible.
    values = []
    for k in range(1, 11):
        model = KMeans(n_clusters=k, random_state=seed, n_init=10).fit(x)
        values.append({"n_clusters": k, "inertia": model.inertia_})
    pd.DataFrame(values).to_csv(TABLES / "elbow_inertia.csv", index=False)
    plt.figure(figsize=(8, 5))
    plt.plot([r["n_clusters"] for r in values],
             [r["inertia"] for r in values], marker="o")
    plt.title("Elbow method")
    plt.xlabel("Number of clusters")
    plt.ylabel("Inertia")
    plt.tight_layout()
    save_figure("elbow_method.png")


def export_scatter_plots(x: np.ndarray, labels: pd.Series,
                         features: list[str]) -> None:
    for a, b in PAIRS:
        plt.figure(figsize=(8, 6))
        plt.scatter(x[:, a], x[:, b], c=labels, s=10, cmap="viridis", alpha=.65)
        plt.xlabel(features[a])
        plt.ylabel(features[b])
        plt.title(f"Original feature scatter: {a} × {b}")
        save_figure(f"scatter_{a}_{b}.png")

    # 17x3 layout from cell 30, with the final variable also plotted.
    fig, axes = plt.subplots(17, 3, figsize=(18, 57), sharex=True)
    for k, ax in enumerate(axes.flat):
        ax.scatter(x[:, 1], x[:, k], c=labels, s=2, cmap="viridis", alpha=.4)
        ax.set_title(features[k], fontsize=9)
    fig.suptitle("Cluster scatter plots by feature (reference: feature 2)")
    fig.tight_layout()
    save_figure("scatter_all_features.png", dpi=80)


def export_centroid_plots(centers: np.ndarray, features: list[str]) -> None:
    # Centroids live in the SCALED feature space, as in the notebook.
    pd.DataFrame(centers, columns=features).rename_axis("Cluster").to_csv(
        TABLES / "cluster_centroids_scaled.csv"
    )
    for a, b in PAIRS:
        plt.figure(figsize=(7, 5))
        plt.scatter(centers[:, a], centers[:, b],
                    c="black", s=200, alpha=.5)
        for i in range(len(centers)):
            plt.annotate(str(i), (centers[i, a], centers[i, b]), xytext=(5, 3),
                         textcoords="offset points")
        plt.xlabel(features[a] + " (scaled)")
        plt.ylabel(features[b] + " (scaled)")
        plt.title(f"Cluster centroids: {a} × {b}")
        save_figure(f"centroids_{a}_{b}.png")


def export_feature_distributions(df: pd.DataFrame,
                                 features: list[str]) -> None:
    # The original notebook defines this plot but does not execute it.
    fig, axes = plt.subplots(17, 3, figsize=(18, 57))
    columns = features + ["DummyInsideShopping", "DummyPrimeZone", "Cluster"]
    # 53 columns would exceed its 51-cell layout; use original 51 model features.
    for name, ax in zip(features, axes.flat):
        sns.histplot(data=df, x=name, ax=ax, bins=30)
        ax.set_title(name, fontsize=9)
        ax.set_xlabel("")
    fig.tight_layout()
    save_figure("feature_distributions.png", dpi=80)


def export_pairplot(df: pd.DataFrame, x: pd.DataFrame) -> None:
    # In the notebook c2 is selected and the first 10 joined columns used:
    # id, ClusterName and the first eight model features. Only the eight
    # numeric features are plotted by seaborn.
    data = x.loc[df["ClusterName"].eq("c2"), x.columns[:8]]
    grid = sns.pairplot(data, diag_kind="hist",
                        plot_kws={"s": 8, "alpha": .5})
    grid.fig.suptitle("Pairplot: original group c2", y=1.005)
    grid.savefig(FIGURES / "pairplot_c2.png", dpi=90, bbox_inches="tight")
    plt.close(grid.fig)


def run(*, workbook: Path = ROOT / "data" / "deparas.xlsx",
        seed: int | None = 42) -> pd.DataFrame:
    """Generate the original notebook's outputs without creating directories."""
    for path in (ASSETS, TABLES, FIGURES):
        if not path.is_dir():
            raise FileNotFoundError(f"Missing pre-existing asset directory: {path}")
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)
    dp, dpuf, dpdummy = read_parameters(workbook)
    df = generate_dataset(dp, dpuf, dpdummy)
    features = [name for name in df.columns if name not in EXCLUDED]
    x = df[features]
    df, x, X, clusters, kmeans = creating_clusters(df, x, 6)

    df.to_csv(ASSETS / "cluster_analysis_dataset.csv", index=False)
    clusters.to_csv(TABLES / "cluster_labels.csv", index=False)
    creates_cluster_pivot_table(df).to_csv(
        TABLES / "cluster_pivot.csv", index=False
    )
    tb = creates_dispersion_table(df, dp)
    tb.to_csv(TABLES / "table_dispersion_notebook.csv", index=False)
    tb.groupby("FeatureGrouping", as_index=False).mean(numeric_only=True).to_csv(
        TABLES / "macro_dispersion_notebook.csv", index=False
    )
    pd.DataFrame([{
        "n_samples": len(df), "n_features": len(features),
        "n_clusters": 6, "init": "random", "n_init": 10, "max_iter": 300,
        "kmeans_random_state": 42, "synthetic_seed": seed,
        "preprocessor": "MinMaxScaler", "inertia": kmeans.inertia_,
    }]).to_csv(TABLES / "cluster_model_notebook.csv", index=False)
    export_elbow(x, seed=seed if seed is not None else 42)
    export_scatter_plots(X, df["Cluster"], features)
    export_centroid_plots(kmeans.cluster_centers_, features)
    export_feature_distributions(df, features)
    export_pairplot(df, x)
    print(f"cluster_analysis: {len(df)} rows, {len(features)} input features, "
          f"clusters={df['Cluster'].nunique()}; assets={ASSETS}")
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path,
                        default=ROOT / "data" / "deparas.xlsx")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    run(workbook=args.workbook, seed=args.seed)


if __name__ == "__main__":
    main()
