# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página / Page configuration
st.set_page_config(layout="wide", page_title="GeoAgro - Dashboard Interativo", page_icon="🌾")

# Carregamento de dados / Data loading
df = pd.read_csv("dados.csv")

# Mapeamento de colunas / Column mapping
colunas_novas = {
    'Safra': 'safra',
    'Regiao': 'regiao',
    'Municipio': 'municipio',
    'Latitude': 'latitude',
    'Longitude': 'longitude',
    'Altitude': 'altitude',
    'Rendimento (Kg/ha)': 'rendimento_kg_ha',
    'Reduçao-chuvas (%)': 'reducao_chuvas_perc',
    'Queda Rendimento 18-19': 'queda_rendimento_perc'
}
df.rename(columns=colunas_novas, inplace=True)

# Função para classificar região por latitude / Function to classify region by latitude
def classificar_regiao(latitude):
    if latitude >= -24:
        return 'Norte_Parana'
    elif latitude < -24 and latitude >= -25.5:
        return 'Centro_Parana'
    else:
        return 'Sul_Parana'

df['regiao_geo'] = df['latitude'].apply(classificar_regiao)

# Título Principal / Main Title
st.title("🌾 GeoAgro Dashboard - Análise de Risco Climático da Soja no Paraná")

# Filtros na Barra Lateral / Sidebar Filters
st.sidebar.header("🎯 Filtros de Visualização / Visualization Filters")
regioes = sorted(df['regiao_geo'].unique())
regiao_selecionada = st.sidebar.selectbox("Selecione uma Região / Select a Region:", regioes)

# Filtragem de dados / Data filtering
df_filtrado = df[df['regiao_geo'] == regiao_selecionada]

st.markdown(f"### Região Selecionada / Selected Region: **{regiao_selecionada}**")

# Visualização de Mapa / Map Visualization
fig = px.scatter_mapbox(
    df_filtrado,
    lat='latitude',
    lon='longitude',
    color='queda_rendimento_perc',
    size='rendimento_kg_ha',
    hover_name='municipio',
    hover_data={
        'rendimento_kg_ha': ':.2f} kg/ha',
        'queda_rendimento_perc': ':.2f}%',
        'reducao_chuvas_perc': ':.2f}%'
    },
    color_continuous_scale=px.colors.sequential.Reds,
    zoom=6,
    height=600
)
fig.update_layout(mapbox_style='open-street-map', margin={'r':0,'t':0,'l':0,'b':0})
st.plotly_chart(fig, use_container_width=True)

# Tabela de Ranking / Ranking Table
st.markdown("#### 📊 Ranking dos Municípios - Queda de Rendimento (%) / Municipality Ranking - Yield Drop (%)")
tabela_resumo = df_filtrado[['municipio', 'rendimento_kg_ha', 'queda_rendimento_perc']].sort_values('queda_rendimento_perc', ascending=False)
st.dataframe(tabela_resumo, use_container_width=True)

# Cálculo de Correlação / Correlation Calculation
st.markdown("#### 🔍 Correlação: Redução de Chuvas e Queda de Rendimento / Correlation: Rainfall Reduction and Yield Drop")
correlacao = df_filtrado[['reducao_chuvas_perc', 'queda_rendimento_perc']].corr().iloc[0,1]
st.metric("Correlação (ρ) / Correlation", f"{correlacao:.2f}")

st.markdown("---")
st.caption("Desenvolvido por Cleverson Moura Andrade — Projeto GeoAgro Risco Soja PR 🌾")
