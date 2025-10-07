import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Carregar dados
df = pd.read_csv('data/metadata.csv')

# Exploração inicial
print("Dimensões do dataset:", df.shape)
print(df.info())
print(df.head())
print("Valores ausentes por coluna:\n", df.isnull().sum())

# Limpeza de dados
df['publication_date'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publication_date'].dt.year
df_clean = df.dropna(subset=['title', 'publication_date'])

# Contagem de palavras do resumo
df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').apply(lambda x: len(x.split()))

# Visualização básica: publicações por ano
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values)
plt.title('Publicações por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Artigos')
plt.show()
