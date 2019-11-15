import pandas as pd
import databaseOrganization as do
from difflib import SequenceMatcher
import numpy as np


def euclidianDistance(x,y):
    return np.sqrt(np.sum((y - x)**2))

def cosineSimilarity(x,y):
    return np.sqrt(np.sum(x*y))/(np.sqrt(np.sum(x**2))*np.sqrt(np.sum(y**2)))

# Definindo função ordenarDicionario().
def ordenarValoresDicionario(dicionario):
    # Variavel auxiliar
    armazenarResultadoOrdenado = []
    for i in sorted(dicionario, key = dicionario.get, reverse = False):
        armazenarResultadoOrdenado.append((i,dicionario[i]))
    return armazenarResultadoOrdenado

def train(data, gameNameData):
    distanceGames = {}
    gameNameX = data[data.index == gameNameData].values
    gameNameX = np.asarray(gameNameX).ravel()
    for index,gameNameY in data.iterrows():
        distanceGames[index] = cosineSimilarity(gameNameX,gameNameY.values)
    return ordenarValoresDicionario(distanceGames)    
    

def similarNames(gameNameUser, allGamesName):
    gamesSimilarNames = []
    for gameNameBase in allGamesName:
        if SequenceMatcher(None,gameNameUser,gameNameBase).ratio() >= 0.75:
            gamesSimilarNames.append(gameNameBase)
    if len(gamesSimilarNames) == 0:
        return None
    else:
        print("Jogo(s) encontrado no banco de dados: {}".format(gamesSimilarNames))
        return allGamesName[gamesSimilarNames[0]]

def recommender(k, gameNameUser):
    data, nameGameID = do.treatDataset()
    gamesNameData = similarNames(gameNameUser, nameGameID)
    if gamesNameData == None:
        print("Nenhum jogo com esse nome foi encontrado!")
    else:
        gamesRecommender = train(data,gamesNameData)
        replaceID = {ID:name for name,ID in zip(nameGameID.keys(),nameGameID.values())}
        for game in gamesRecommender[1:k+1]:
            print(replaceID[game[0]])
        