import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("/home/bevilacqua/.cache/kagglehub/datasets/gustavomartino/brasileirao/versions/2/CampBras.csv")

def mostrar_jogos_santos(df):
    # Filtra apenas os jogos em que o Santos é o time da casa e mais que 5 gols
    santos_em_casa = df[(df["hometeam"]=="Santos") & (df["goalsht"]>5)]
    print(santos_em_casa)

def mostrar_jogos_santosxcorinthians(df):
    # Filtra apenas os jogos entre Corinthians e Santo
    santosxcorinthians = df[((df["hometeam"] == "Santos") & (df["visitingteam"] == "Corinthians")) |
                                  ((df["hometeam"] == "Corinthians") & (df["visitingteam"] == "Santos"))]
    print(santosxcorinthians)

def vitoria_santos(df):
    # Filtra as vitórias
    santosvictory = df[((df["hometeam"] == "Santos") & (df["goalsht"] > df["goalsvt"])) | 
                        ((df["visitingteam"] == "Santos") & (df["goalsvt"] > df["goalsht"]))]
    vitoria_count = len(santosvictory)
    jogos_santos = df[(df["hometeam"] == "Santos") | (df["visitingteam"] == "Santos")]
    total_jogos = len(jogos_santos)
    porcentagem_vitoria = (vitoria_count / total_jogos) * 100
    print(f"Vitórias: {vitoria_count} ({porcentagem_vitoria:.2f}%)")
    print(santosvictory)

def derrota_santos(df):
    santosdefeat = df[((df["hometeam"] == "Santos") & (df["goalsht"] < df["goalsvt"])) | 
                       ((df["visitingteam"] == "Santos") & (df["goalsvt"] < df["goalsht"]))]
    derrota_count = len(santosdefeat)
    jogos_santos = df[(df["hometeam"] == "Santos") | (df["visitingteam"] == "Santos")]
    total_jogos = len(jogos_santos)
    porcentagem_derrota = (derrota_count / total_jogos) * 100
    print(f"Derrotas: {derrota_count} ({porcentagem_derrota:.2f}%)")

def empate_santos(df):
    santosigual = df[((df["hometeam"] == "Santos") & (df["goalsht"] == df["goalsvt"])) | 
                      ((df["visitingteam"] == "Santos") & (df["goalsvt"] == df["goalsht"]))]
    empate_count = len(santosigual)
    jogos_santos = df[(df["hometeam"] == "Santos") | (df["visitingteam"] == "Santos")]
    total_jogos = len(jogos_santos)
    porcentagem_empate = (empate_count / total_jogos) * 100
    print(f"Empates: {empate_count} ({porcentagem_empate:.2f}%)")
    print(total_jogos)


def diadejogo(dia, mes, ano):
    matchday = df[(df["day"]== dia) & (df["month"]== mes) & (df["year"]== ano)]
    print(matchday)

def rodada(rodada, ano):
    rodaday = df[(df["round"] == rodada) & (df["year"]== ano)]
    print(rodaday)

def jogostime(time, temporada):
    aux = df[(((df["hometeam"] == time) | (df["visitingteam"] == time)) & (df["season"] == temporada))]
    print(aux)

def jogostimes(time, time2):
    aux = df[(((df["hometeam"] == time) | (df["visitingteam"] == time)) & ((df["hometeam"] == time2) | (df["visitingteam"] == time2)))]
    print(aux)


def mediaGolsCasa(time, temporada):
    jogos = df[((df["hometeam"] == time) & (df["season"] == temporada))]
    mediaGols = round(jogos["goalsht"].mean(),3)
    print(mediaGols)

def mediaGolsTemporada(time, temporada):
    jogosH = df[((df["hometeam"] == time) & (df["season"] == temporada))]
    jogosV = df[((df["visitingteam"] == time) & (df["season"] == temporada))]
    mediaGolsH = round(jogosH["goalsht"].mean(),3)
    mediaGolsV = round(jogosV["goalsvt"].mean(),3)
    mediaGolsGeral = round((mediaGolsH+mediaGolsV) / 2, 3)
    print("Médias de Gols em Casa: ",mediaGolsH)
    print("Médias de Gols Fora de Casa: ",mediaGolsV)
    print("Médias de Gols na Temporada por jogo: ",mediaGolsGeral)

def mediaGolsTemporada(temporada):
    
    aux = df[(df["season"] == temporada)]
    goalsH = aux["goalsht"].sum()
    goalsV = aux["goalsvt"].sum()
    goalsG = (goalsH+goalsV)
    goalsGR = goalsG/38
    goalsGRT = goalsGR/10
    goalsHMedia = goalsH/38
    goalsVMedia = goalsV/38

    print("Total de Gols de equipes da Casa: ", goalsH)
    print("Total de Gols de equipes Visitantes: ", goalsV)
    print("Total de Gols Geral: ", goalsG)
    print("Média de Gols dos times da casa por rodada: ", goalsHMedia)
    print("Média de Gols dos times visitantes por rodada: ", goalsVMedia)
    print("Média de Gols por rodada: ", goalsGR)
    print("Méida de Gols por jogo: ", goalsGRT)




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
#rodada(38,2015)
#jogostime("Grêmio", 2015)
#jogostimes("Cruzeiro", "Grêmio")
#mediaGolsTemporada("Grêmio", 2019)
#mediaGolsTemporada(2019)