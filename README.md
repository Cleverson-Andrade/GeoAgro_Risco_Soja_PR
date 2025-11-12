# 🗺️ GeoAgro_Risco_Soja_PR: Dashboard de Análise de Risco Geo-Climático

## Resumo Executivo
Este projeto simula uma análise crítica de Geo-localização de risco, focada em correlacionar o estresse climático (redução de chuvas) com a produtividade agrícola. 
O objetivo é fornecer um dashboard interativo que auxilie na identificação rápida de áreas de alto estresse climático para a soja.

---

## 🚀 Dashboard Interativo

O projeto está totalmente funcional e disponível publicamente para exploração:

**[CARREGANDO]**

---

## 📚 Fonte e Referência dos Dados
Os dados utilizados neste projeto são de acesso público e foram obtidos diretamente da pesquisa agrícola brasileira:

* **Fonte Principal:** EMBRAPA - Repositório de Dados de Pesquisa (REDAPE).
* **Referência Específica:** ( https://www.redape.dados.embrapa.br/file.xhtml?fileId=5772&datasetVersionId=556 )
    *(A análise foi focada nas variáveis climáticas e de rendimento presentes neste dataset.)*

---

## 📊 O Que Foi Feito: Análise de Dados

O trabalho focado em Ciência de Dados incluiu as seguintes etapas:

1.  **Limpeza e ETL:** Tratamento completo dos dados brutos, padronização de colunas e formatação numérica.
2.  **Engenharia de Atributos Geo-espaciais:** Criação da segmentação de `regiao_geo` a partir das coordenadas geográficas.
3.  **Insight Chave:** Comprovação de uma forte correlação positiva (ρ ≈ 0.89) entre a Redução de Chuvas e a Queda de Rendimento.
4.  **Entrega:** Criação de um Mapa de Calor Interativo em Plotly.

---

## 💻 Como Rodar Localmente
Para rodar, basta clonar o repositório, instalar as dependências (pandas, plotly, streamlit) via `requirements.txt` e executar:
`streamlit run app.py`
