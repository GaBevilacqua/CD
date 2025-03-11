import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("/home/bevilacqua/.cache/kagglehub/datasets/gustavomartino/brasileirao/versions/2/CampBras.csv")

def mostrar_jogos_santos(df):
    # Filtra apenas os jogos em que o Santos é o time da casa e mais que 5 gols
    santos_em_casa = df[(df["hometeam"]=="Santos") & (df["goalsht"]>5)]
    # Exibe os jogos
    print(santos_em_casa)

def mostrar_jogos_santosxcorinthians(df):
    # Filtra apenas os jogos em que o Santos é o time da casa e mais que 5 gols
    santosxcorinthians = df[((df["hometeam"] == "Santos") & (df["visitingteam"] == "Corinthians")) |
                                  ((df["hometeam"] == "Corinthians") & (df["visitingteam"] == "Santos"))]
    # Exibe os jogos
    print(santosxcorinthians)

#Primeiras Linhas
#print(df.head())

#tipo de dados
#print(df.info())

#descrições básicas
#print(df.describe())

#Array das colunas
#print(df.columns)# Contagem dos jogos em casa por time (hometeam)



#mostrar_jogos_santos(df)
mostrar_jogos_santosxcorinthians(df)