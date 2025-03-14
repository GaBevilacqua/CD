import pandas as pd
import matplotlib.pyplot as plt

# Tente carregar o arquivo com uma codificação diferente
df = pd.read_csv('/home/bevilacqua/Documents/CD/FoodImports.csv', encoding='latin1')

# Exibir as primeiras linhas
print(df.head())

def CountriesByCategory(pais, categoria):
    aux = df[(df["Country"] == pais) & (df["Category"] == categoria)]
    print(aux)

def Year(ano):
    aux = df[df["Year Number"] == ano]
    print(aux)

def Country(pais):
    aux = df[df["Country"] == pais]
    print(aux)

# Função para gerar um gráfico de importação ao longo dos anos para um país
def plot_imports_by_year(pais):
    aux = df[df["Country"] == pais].groupby("Year Number")["Value"].sum().reset_index()

    plt.figure(figsize=(10, 5))
    plt.bar(aux["Year Number"], aux["Value"], color="skyblue")
    plt.xlabel("Ano")
    plt.ylabel("Valor das Importações (Milhões $)")
    plt.title(f"Importações de {pais} ao longo dos anos")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("importacoes.png")  # Salva o gráfico como imagem
    plt.close()  # Fecha a figura para liberar memória
    plt.show()

# Exemplo de uso da função
plot_imports_by_year("BRAZIL")
