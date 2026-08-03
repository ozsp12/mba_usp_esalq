# Retail Bank Branch Clustering

This repository contains the capstone project developed for the MBA in Big Data and Analytics at USP/ESALQ.

## Project overview

The project presents a clustering-based methodology for reducing the analytical complexity of retail banking networks. The K-means algorithm is used to group thousands of bank branches into six comparable clusters. Branches assigned to the same cluster share similar behavioral and operational characteristics and can therefore be evaluated against comparable performance targets.

The resulting clusters exhibit low within-cluster dispersion and clear differences between clusters. All data used in the analysis are synthetic. They were generated from statistical distributions calibrated with real retail-banking data to prevent the disclosure of confidential or personal information and to comply with Brazil's General Data Protection Law (Lei Geral de Proteção de Dados, LGPD).

## Repository structure

```text
.
├── data/          Synthetic-data metadata and analytical outputs
├── notebooks/     Data-generation and clustering notebooks
├── thesis/        Capstone manuscript, project document, and presentation
├── README.md      Project description and file guide
└── REFERENCES.md  Complete bibliography
```

## Notebooks

- [`create_dataframes.ipynb`](notebooks/create_dataframes.ipynb) generates the synthetic modeling data from the metadata workbooks.
- [`cluster_analysis.ipynb`](notebooks/cluster_analysis.ipynb) performs K-means clustering, statistical analyses, and visualizations.

The notebooks preserve the original project environment. Package versions are not pinned, so minor adjustments may be necessary when running them with newer Python distributions.

## Data files

- [`deparas.xlsx`](data/deparas.xlsx) contains the metadata used to generate the synthetic data. Its worksheets define feature means and standard deviations, dummy-variable probabilities, the distribution of branches by Brazilian state, cluster descriptions, and auxiliary intensity scales.
- [`cluster_analysis.xlsx`](data/cluster_analysis.xlsx) contains clustering results and analytical outputs.
- [`table_dispersion.xlsx`](data/table_dispersion.xlsx) contains within-cluster dispersion statistics.
- [`tables.xlsx`](data/tables.xlsx) contains supporting tables used by the analysis.

## Thesis and presentation

The [`thesis/`](thesis/) directory contains the final manuscript in DOCX and PDF formats, the original capstone proposal, and the defense presentation in PPTX and PDF formats.

## References

The complete bibliography is available in [`REFERENCES.md`](REFERENCES.md). It includes the foundational K-means paper, studies of clustering in banking, locally adaptive metrics, and references on synthetic-data generation.

## Author

**Osvaldo Luiz dos Santos Pereira**

- [Academic webpage](https://ozsp12.github.io/)
- [Currículo Lattes](http://lattes.cnpq.br/6730251976463283)
- [ORCID](https://orcid.org/0000-0003-2231-517X)
- [Google Scholar](https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en)
- [ResearchGate](https://www.researchgate.net/profile/Osvaldo-Santos-Pereira)
- [GitHub](https://github.com/ozsp12)
- [LinkedIn](https://www.linkedin.com/in/ozsp12)
- [Substack](https://substack.com/@olsp1982)
- [Medium](https://medium.com/@ozsp12)
- [YouTube](https://www.youtube.com/@ozlsp12)
- [TikTok](https://www.tiktok.com/@ozsp12)
- [Patreon](https://www.patreon.com/ozsp12)
- [X](https://x.com/ozsp12)

## License and reuse

No explicit open-source license is currently provided. Consequently, the repository may be viewed and referenced, but reuse, redistribution, or modification is not automatically authorized.
