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
    # Filtra apenas os jogos entre Corinthians e Santo
    santosxcorinthians = df[((df["hometeam"] == "Santos") & (df["visitingteam"] == "Corinthians")) |
                                  ((df["hometeam"] == "Corinthians") & (df["visitingteam"] == "Santos"))]
    # Exibe os jogos
    print(santosxcorinthians)

def vitoria_santos(df):
    # Filtra as vitórias
    santosvictory = df[((df["hometeam"] == "Santos") & (df["goalsht"] > df["goalsvt"])) | 
                        ((df["visitingteam"] == "Santos") & (df["goalsvt"] > df["goalsht"]))]
    # Número de vitórias
    vitoria_count = len(santosvictory)
    
    # Filtra todos os jogos do Santos
    jogos_santos = df[(df["hometeam"] == "Santos") | (df["visitingteam"] == "Santos")]
    total_jogos = len(jogos_santos)
    
    # Cálculo da porcentagem de vitórias
    porcentagem_vitoria = (vitoria_count / total_jogos) * 100
    
    # Exibe os resultados
    print(f"Vitórias: {vitoria_count} ({porcentagem_vitoria:.2f}%)")
    print(santosvictory)

def derrota_santos(df):
    # Filtra as derrotas
    santosdefeat = df[((df["hometeam"] == "Santos") & (df["goalsht"] < df["goalsvt"])) | 
                       ((df["visitingteam"] == "Santos") & (df["goalsvt"] < df["goalsht"]))]
    # Número de derrotas
    derrota_count = len(santosdefeat)
    
    # Filtra todos os jogos do Santos
    jogos_santos = df[(df["hometeam"] == "Santos") | (df["visitingteam"] == "Santos")]
    total_jogos = len(jogos_santos)
    
    # Cálculo da porcentagem de derrotas
    porcentagem_derrota = (derrota_count / total_jogos) * 100
    
    # Exibe os resultados
    print(f"Derrotas: {derrota_count} ({porcentagem_derrota:.2f}%)")

def empate_santos(df):
    # Filtra os empates
    santosigual = df[((df["hometeam"] == "Santos") & (df["goalsht"] == df["goalsvt"])) | 
                      ((df["visitingteam"] == "Santos") & (df["goalsvt"] == df["goalsht"]))]
    # Número de empates
    empate_count = len(santosigual)
    
    # Filtra todos os jogos do Santos
    jogos_santos = df[(df["hometeam"] == "Santos") | (df["visitingteam"] == "Santos")]
    total_jogos = len(jogos_santos)
    
    # Cálculo da porcentagem de empates
    porcentagem_empate = (empate_count / total_jogos) * 100
    
    # Exibe os resultados
    print(f"Empates: {empate_count} ({porcentagem_empate:.2f}%)")
    print(total_jogos)

def diadejogo(dia, mes, ano):
    matchday = df[(df["day"]== dia) & (df["month"]== mes) & (df["year"]== ano)]
    print(matchday)

def rodada(rodada, ano):
    rodaday = df[(df["round"] == rodada) & (df["year"]== ano)]
    print(rodaday)


#Primeiras Linhas
#print(df.head())

#tipo de dados
#print(df.info())

#descrições básicas
#print(df.describe())

#Array das colunas
#print(df.columns)# Contagem dos jogos em casa por time (hometeam)



#mostrar_jogos_santos(df)
#mostrar_jogos_santo(df["day"]== dia)sxcorinthians(df)
#vitoria_santos(df)
#derrota_santos(df)
#empate_santos(df)
#diadejogo(5,8,2018)
rodada(38,2015)