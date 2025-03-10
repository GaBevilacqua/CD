import pandas as pd
df = pd.read_csv("/home/bevilacqua/.cache/kagglehub/datasets/gustavomartino/brasileirao/versions/2/CampBras.csv")

#Primeiras Linhas
#print(df.head())

#tipo de dados
#print(df.info())

#descrições básicas
#print(df.describe())

#Array das colunas
#print(df.columns)

df.groupby("hometeam")["goalsht"].sum().sort_values(ascending=False)