# 🗺️ GeoAgro_Risco_Soja_PR: Dashboard de Análise de Risco Geo-Climático

## Resumo Executivo
Este projeto simula uma análise crítica de geolocalização de risco, com foco em correlacionar o estresse climático (redução de chuvas) com a produtividade agrícola.  
O objetivo é oferecer um dashboard interativo que facilite a identificação de áreas com alto risco climático para o cultivo de soja no estado do Paraná.

---

## 🚀 Dashboard Interativo
O projeto está totalmente funcional e disponível publicamente para exploração:

**(https://geoagroriscosojapr-dbi2ch2yrac2ftm9hy9ewo.streamlit.app/)**

---

## 📚 Fonte e Referência dos Dados
Os dados utilizados neste projeto são de acesso público e foram obtidos diretamente da pesquisa agrícola brasileira:

- **Fonte principal:** EMBRAPA – Repositório de Dados de Pesquisa (REDAPE).  
- **Referência específica:** (https://www.redape.dados.embrapa.br/file.xhtml?fileId=5772&datasetVersionId=556)

A análise concentrou-se nas variáveis climáticas e de rendimento contidas nesse conjunto de dados.

---

## 📊 O Que Foi Feito
O trabalho de análise de dados envolveu as seguintes etapas:

1. **Limpeza e ETL:** tratamento completo dos dados brutos, padronização de colunas e formatação numérica.  
2. **Engenharia de atributos geo-espaciais:** criação da segmentação de `regiao_geo` a partir das coordenadas geográficas.  
3. **Insight principal:** identificação de uma correlação positiva forte (ρ ≈ 0.89) entre redução de chuvas e queda de rendimento.  
4. **Entrega:** construção de um mapa interativo (Plotly) para visualização espacial dos impactos climáticos.

---

## 🧩 Estrutura do Repositório

O repositório foi organizado em duas versões complementares, adequadas para diferentes contextos de uso:

- **Dados_soja_parana_colab.ipynb**  
  Versão exploratória e analítica, desenvolvida para o ambiente Google Colab ou Jupyter Notebook.  
  Utiliza `display()` e `print()` para exibir resultados de forma direta e formatada dentro do notebook.  
  
- **Dados_soja_parana_streamlit.py**  
  Versão adaptada para o Streamlit, utilizando `st.write()` e `st.dataframe()` em substituição aos comandos do notebook.  

- **dados.csv**  
  Conjunto de dados utilizado na análise, contendo variáveis climáticas e de produtividade.

- **requirements.txt**  
  Arquivo de dependências necessárias para execução local do projeto.

---
   ```bash
   git clone https://github.com/seuusuario/GeoAgro_Risco_Soja_PR.git
