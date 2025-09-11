# mba_usp_esalq
Este repositório contém todos os arquivos do trabalho de conclusão de curso do MBA em Big Data e Analytics da USP-ESALQ

# Resumo do trabalho
Neste trabalho foi apresentada metodologia sobre como reduzir a dimensão de análises no nicho de bancos de varejo através da utilização de algoritmos de clusterização. Foi utilizado o algoritmo K-Means para reduzir a quantidade de milhares de agências de um determinado banco de varejo para apenas seis grupos comparáveis (clusters) para os quais foram aplicados metas de performance semelhantes. Foi demonstrado neste trabalho que o K-means teve uma performance adequada em agrupar as agências em grupos semelhantes de acordo com as variáveis de comportamento e de características, o resultado final apresentou baixa dispersão das variáveis dentro dos clusters e diferenciando estas mesmas variáveis entre os clusters. Os dados utilizados foram gerados sinteticamente em cumprimento da Lei Geral de Proteção aos Dados (LGPD) à partir de métodos estatísticos e baseados em dados reais de um determinado banco de varejo.

# Referências
- MacQueen, J.B. (1967). Some Methods for classification and Analysis of Multivariate Observations. Proceedings of 5th Berkeley Symposium on Mathematical Statistics and Probability. Vol. 1. University of California Press. pp. 281–297. 
- Tang, G.;  Tian, R.; Wu, B. (2022). An Overview of Clustering Methods in The Financial World. Proceedings of the 2022 7th International Conference on Financial Innovation and Economic Development Atlantis Press.
- Herrera-Restrepo, O.; Triantis, K.; Seaver, W.L.; Paradi, J.C.; Zhu, H.; Bank branch operational performance: A robust multivariate and clustering approach, Expert Systems with Applications, Volume 50, 2016, Pages 107-119, ISSN 0957-4174.
- Marques, B.P.; Alves,C.F. (2020) Using clustering ensemble to identify banking business models. Intell Sys Acc Fin Mgmt. 27: 66– 94.  
- Domeniconi, C.; Gunopulos, D.; Ma, S.; Papadopoulos, D.; Yan, B. (2007) Locally adaptive metrics for clustering high dimensional data. Data Mining and Knowledge Discovery, Volume 14, Issue 1, pp 63–97. 
- Sharahi, M.; Aligholi, M. (2015) Classify the Data of Bank Customers Using Data Mining and   Clustering Techniques (Case Study: Sepah Bank Branches Tehran), J. Appl. Environ. Biol. Sci., 5(5) 458-464.
- T. E. Raghunathan, Synthetic data, Annual Review of Statistics and Its Application, 8, 129-140, 2021.
- Dankar, K.; Mahmoud, I. (2021) Fake it till you make it: guidelines for effective synthetic data generation, Applied Sciences 11.5: 2158.
- Hradec, J.; Craglia, M.; Di Leo, M.; De Nigris, S.; Ostlaender, N.; Nicholson, N. (2022) Multipurpose synthetic population for policy applications, EUR 31116 EN, Publications Office of the European Union, Luxembourg, ISBN 978-92-76-53478-5.

# Arquivos
* [deparas.xlsx](https://github.com/Osvaldo1982/mba_usp_esalq/blob/main/deparas.xlsx): arquivo do tipo Excel contendo os metadados para a criação dos dados sintéticos utilizados no projeto. O arquivo contém as seguintes abas
  * ProbsFeatures: contém os valores de média e desvio padrão para cada uma das cinquenta e uma variáveis de clusterização para ocorrência e valores destas variáveis para cada um dos seis clusters criados. É a tabela central utilizada na metodologia para geração dos dados sintéticos e do dataframe de modelagem.
  * Dummy: contém o metadados das probabilidades de ocorrência das variáveis dummy DummyInsideShopping e DummyPrimeZone.
  * State: contém o metadados com a distribuição de probabilidade de ocorrência de agências por Estado brasileiro (UF).
  * ds_cluster: contém a agregação das variáveis de clusterização com a descrição das características de negócios de cada um dos clusters.
  * Aux: Contém metadados auxiliares, não é utilizado diretamente na metodologia.
  * Dpintensity: contém depara de intensidades utilizado para designar os valores para médias e desvios padrões de cada uma das variáveis de caracterização das agências.
  * Dpds: contém o metadados geral de médias, desvios e intensidades para cada um dos clusters criados. É utilizado auxiliarmente para gerar a tabela ProbFeatures.

* [ClusterAnalysis.ipynb](https://github.com/Osvaldo1982/mba_usp_esalq/blob/main/cluster_analysis.ipynb): arquivo notebook jupyter contendo o algoritmo de geração de clusters, e algumas análises de clusterização, investigações estatísticas, e gráficos.
* [table_dispersion.xlsx](https://github.com/Osvaldo1982/mba_usp_esalq/blob/main/table_dispersion.xlsx):
* [cluster_analise.xlsx](https://github.com/Osvaldo1982/mba_usp_esalq/blob/main/cluster_analise.xlsx):
* [tcc_mba_usp_esalq_ds_osvaldo_pereira](https://github.com/Osvaldo1982/mba_usp_esalq/blob/main/tcc_mba_usp_esalq_ds_osvaldo_pereira_20230211.docx)

# Social Media
🌐 Webpage: https://ozsp12.github.io/  
✅ GitHub: https://github.com/ozsp12  
🧪 ResearchGate: https://www.researchgate.net/profile/Osvaldo-Santos-Pereira  
🔬 Google Scholar: https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en  
🧾 ORCID: https://orcid.org/0000-0003-2231-517X  
💼 LinkedIn: https://www.linkedin.com/in/ozsp12  
🧡 Patreon: https://www.patreon.com/ozsp12  
✍️ Medium: https://medium.com/@ozsp12  
𝕏  X (Twitter): https://x.com/ozsp12  
📱 TikTok: https://www.tiktok.com/@ozsp12  
▶️ YouTube: https://www.youtube.com/@ozlsp12  

