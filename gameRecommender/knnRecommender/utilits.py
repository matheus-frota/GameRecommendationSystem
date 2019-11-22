import numpy as np
from difflib import SequenceMatcher



def euclidianDistance(x,y):
    return np.sqrt(np.sum((y - x)**2))

def cosineSimilarity(x,y):
    return np.sqrt(np.sum(x*y))/(np.sqrt(np.sum(x**2))*np.sqrt(np.sum(y**2)))

def sortValueDict(dictionary):
    storeOrderedResult = []
    for i in sorted(dictionary, key = dictionary.get, reverse = False):
        storeOrderedResult.append((i,dictionary[i]))
    return storeOrderedResult

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