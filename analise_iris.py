# =====================================================
# Tarefa: Carregamento, análise e visualização de dados
# Objetivo: Explorar dados usando pandas e visualizá-los com matplotlib/seaborn
# =====================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Configurações de estilo para gráficos
sns.set(style="whitegrid")

def main():
    print("=== Análise de Dados Iris ===\n")

    try:
        # Carregando o dataset Iris via sklearn
        iris_data = load_iris()
        df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
        df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

        # ================================
        # Etapas de exploração do conjunto
        # ================================
        print("Primeiras 5 linhas do dataset:")
        print(df.head(), "\n")

        print("Informações do dataset:")
        print(df.info(), "\n")

        print("Valores ausentes por coluna:")
        print(df.isnull().sum(), "\n")

        # Limpeza de dados: preencher valores ausentes (se houvesse)
        df.fillna(method='ffill', inplace=True)

        # =================================
        # Análise básica de dados
        # =================================
        print("Estatísticas descritivas das colunas numéricas:")
        print(df.describe(), "\n")

        # Agrupamento por espécie
        agrupamento = df.groupby('species').mean()
        print("Média de cada feature por espécie:")
        print(agrupamento, "\n")

        # =================================
        # Visualizações
        # =================================

        # 1️⃣ Gráfico de linhas: média das features por espécie
        agrupamento.plot(kind='line', marker='o', title="Média das features por espécie")
        plt.ylabel("Média")
        plt.xlabel("Feature")
        plt.legend(title="Espécie")
        plt.show()

        # 2️⃣ Gráfico de barras: comprimento médio da pétala por espécie
        sns.barplot(x='species', y='petal length (cm)', data=df)
        plt.title("Comprimento médio da pétala por espécie")
        plt.ylabel("Comprimento da pétala (cm)")
        plt.xlabel("Espécie")
        plt.show()

        # 3️⃣ Histograma: distribuição do comprimento da sépala
        sns.histplot(df['sepal length (cm)'], bins=15, kde=True)
        plt.title("Distribuição do comprimento da sépala")
        plt.xlabel("Comprimento da sépala (cm)")
        plt.show()

        # 4️⃣ Gráfico de dispersão: comprimento da sépala vs comprimento da pétala
        sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
        plt.title("Comprimento da sépala vs comprimento da pétala")
        plt.xlabel("Comprimento da sépala (cm)")
        plt.ylabel("Comprimento da pétala (cm)")
        plt.show()

        # Observações
        print("\nObservações:")
        print("- Setosa tem pétalas e sépalas menores que Versicolor e Virginica.")
        print("- Virginica tende a ter pétalas maiores que Versicolor.")
        print("- Há clara separação entre as espécies observando pétalas e sépalas.\n")

    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: arquivo CSV vazio.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
