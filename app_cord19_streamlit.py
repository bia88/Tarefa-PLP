import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Explorador de Dados CORD-19")
st.write("Análise simples de artigos sobre COVID-19")
sns.set(style="whitegrid")

# Carregar dados
df = pd.read_csv('data/metadata.csv')
df['publication_date'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publication_date'].dt.year
df_clean = df.dropna(subset=['title', 'publication_date'])

# Widget: intervalo de anos
year_range = st.slider("Selecione intervalo de anos", 2019, 2025, (2020, 2021))
df_filtered = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]

# Gráfico: publicações por ano
year_counts = df_filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Mostrar amostra dos dados
st.write(df_filtered.head())
