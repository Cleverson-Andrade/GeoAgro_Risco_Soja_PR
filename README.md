# 🗺️ GeoAgro_Risco_Soja_PR: Dashboard de Análise de Risco Geo-Climático

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

[English](#english) • [Português](#portugues)

---

<a name="english"></a>
## 🇺🇸 English

### 📝 Project Overview
This project performs a geo-location risk analysis, focusing on correlating climatic stress (rainfall reduction) with soybean agricultural productivity in Paraná, Brazil. The goal is to provide an interactive dashboard to identify high-risk areas for crop management.

### 🚀 Interactive Dashboard
The project is live and public:
🔗 **[Access Dashboard on Streamlit](https://geoagroriscosojapr-dbi2ch2yrac2ftm9hy9ewo.streamlit.app/)**

### 📊 Key Achievements
1. **ETL & Data Cleaning:** Full processing of raw data, standardizing columns, and numeric formatting.
2. **Geo-Spatial Engineering:** Segmented data into `regiao_geo` based on geographical coordinates.
3. **Core Insight:** Identified a strong positive correlation (ρ ≈ 0.89) between rainfall reduction and yield drop.
4. **Delivery:** Interactive Map (Plotly) for spatial visualization of climatic impacts.

---

<a name="portugues"></a>
## 🇧🇷 Português

### 📝 Resumo Executivo
Este projeto realiza uma análise crítica de geolocalização de risco, correlacionando o estresse climático (redução de chuvas) com a produtividade agrícola da soja no Paraná. O objetivo é oferecer um dashboard interativo para identificação de áreas de alto risco.

### 🚀 Dashboard Interativo
O projeto está disponível publicamente:
🔗 **[Acessar Dashboard no Streamlit](https://geoagroriscosojapr-dbi2ch2yrac2ftm9hy9ewo.streamlit.app/)**

### 📊 WHAT Foi Feito
1. **Limpeza e ETL:** Tratamento completo dos dados brutos e padronização de colunas.
2. **Engenharia de Atributos:** Criação da segmentação `regiao_geo` a partir de coordenadas geográficas.
3. **Insight Principal:** Identificação de correlação forte (ρ ≈ 0.89) entre falta de chuva e queda de rendimento.
4. **Entrega:** Construção de mapa interativo (Plotly) para visualização espacial.

---

## 📚 Data Source / Fonte dos Dados
* **EMBRAPA** – Repositório de Dados de Pesquisa (REDAPE).
* **Reference:** [Access Data Here](https://www.redape.dados.embrapa.br/file.xhtml?fileId=5772&datasetVersionId=556).

---

## 🧩 Repository Structure / Estrutura do Repositório

- **`Dados_soja_parana_colab.ipynb`** Exploratory analysis for Google Colab/Jupyter.
- **`Dados_soja_parana_streamlit.py`** Production version for Streamlit Dashboard.
- **`dados.csv`** Dataset containing climate and productivity variables.
- **`requirements.txt`** Project dependencies.

---
👤 **Author / Autor:** Cleverson Moura Andrade
