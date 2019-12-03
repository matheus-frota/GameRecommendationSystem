import numpy as np
import pandas
from difflib import SequenceMatcher


def euclidianDistance(x,y):
    return np.sqrt(np.sum((y - x)**2))

def cosineSimilarity(x,y):
    #return np.sqrt(np.sum(x*y))/(np.sqrt(np.sum(x**2))*np.sqrt(np.sum(y**2)))
    return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

def sortValueDict(dictionary):
    storeOrderedResult = []
    for i in sorted(dictionary, key = dictionary.get, reverse = True):
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

def cosineSimilarityMatrix(data):
    cosineSimilarityDictionary = {}
    for nameColumnGame,valueColumnGame in data.iterrows():
        temporaryList = []
        for nameRowGame,valueRowGame in data.iterrows():
            temporaryList.append(cosineSimilarity(valueColumnGame.values,valueRowGame.values))
        cosineSimilarityDictionary[nameColumnGame] = temporaryList
    return pandas.DataFrame.from_dict(cosineSimilarityDictionary)

def meanUpperTriangleMatrix(matrix):
    totalNumbers = sum(list(range(1,matrix.shape[0])))
    sumMatrix = matrix.sum()
    return sumMatrix/totalNumbers