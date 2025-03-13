import pandas as pd

# Tente carregar o arquivo com uma codificação diferente
df = pd.read_csv('/home/bevilacqua/Documents/CD/FoodImports.csv', encoding='latin1')

# Exibir as primeiras linhas
print(df.head())