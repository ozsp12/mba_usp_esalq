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

<a href="mailto:olsp@if.ufrj.br"><img src="https://api.iconify.design/mdi:email.svg?color=%23888888" height="22" alt="Email" align="absmiddle"></a> **Email:** [olsp@if.ufrj.br](mailto:olsp@if.ufrj.br)  
<a href="https://ozsp12.github.io/"><img src="https://api.iconify.design/mdi:web.svg?color=%23888888" height="22" alt="Academic webpage" align="absmiddle"></a> **Academic webpage:** [https://ozsp12.github.io/](https://ozsp12.github.io/)  
<a href="http://lattes.cnpq.br/6730251976463283"><img src="https://api.iconify.design/mdi:account-school.svg?color=%23888888" height="22" alt="Lattes" align="absmiddle"></a> **Lattes:** [http://lattes.cnpq.br/6730251976463283](http://lattes.cnpq.br/6730251976463283)  
<a href="https://orcid.org/0000-0003-2231-517X"><img src="https://cdn.simpleicons.org/orcid/A6CE39" height="22" alt="ORCID" align="absmiddle"></a> **ORCID:** [https://orcid.org/0000-0003-2231-517X](https://orcid.org/0000-0003-2231-517X)  
<a href="https://scholar.google.com/citations?user=HIZp0X8AAAAJ&amp;hl=en"><img src="https://cdn.simpleicons.org/googlescholar/4285F4" height="22" alt="Google Scholar" align="absmiddle"></a> **Google Scholar:** [https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en](https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en)  
<a href="https://www.researchgate.net/profile/Osvaldo-Santos-Pereira"><img src="https://cdn.simpleicons.org/researchgate/00CCBB" height="22" alt="ResearchGate" align="absmiddle"></a> **ResearchGate:** [https://www.researchgate.net/profile/Osvaldo-Santos-Pereira](https://www.researchgate.net/profile/Osvaldo-Santos-Pereira)  
<a href="https://github.com/ozsp12"><img src="https://cdn.simpleicons.org/github/888888" height="22" alt="GitHub" align="absmiddle"></a> **GitHub:** [https://github.com/ozsp12](https://github.com/ozsp12)  
<a href="https://br.linkedin.com/in/ozsp12"><img src="https://api.iconify.design/mdi:linkedin.svg?color=%230A66C2" height="22" alt="LinkedIn" align="absmiddle"></a> **LinkedIn:** [https://br.linkedin.com/in/ozsp12](https://br.linkedin.com/in/ozsp12)  
<a href="https://substack.com/@olsp1982"><img src="https://cdn.simpleicons.org/substack/FF6719" height="22" alt="Substack" align="absmiddle"></a> **Substack:** [https://substack.com/@olsp1982](https://substack.com/@olsp1982)  
<a href="https://medium.com/@ozsp12"><img src="https://cdn.simpleicons.org/medium/888888" height="22" alt="Medium" align="absmiddle"></a> **Medium:** [https://medium.com/@ozsp12](https://medium.com/@ozsp12)  
<a href="https://www.youtube.com/@ozlsp12"><img src="https://cdn.simpleicons.org/youtube/FF0000" height="22" alt="YouTube" align="absmiddle"></a> **YouTube:** [https://www.youtube.com/@ozlsp12](https://www.youtube.com/@ozlsp12)  
<a href="https://x.com/ozsp12"><img src="https://cdn.simpleicons.org/x/888888" height="22" alt="X" align="absmiddle"></a> **X:** [https://x.com/ozsp12](https://x.com/ozsp12)

## License and reuse

No explicit open-source license is currently provided. Consequently, the repository may be viewed and referenced, but reuse, redistribution, or modification is not automatically authorized.
