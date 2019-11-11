import pandas as pd
import databaseOrganization as do
from difflib import SequenceMatcher


def train(data, gameNameUser):

    print(data)
    

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
    data, nameGameID = do.filterDataset()
    gamesNameData = similarNames(gameNameUser, nameGameID)
    if gamesNameData == None:
        print("Nenhum jogo com esse nome foi encontrado!")
    else:
        print(gamesNameData)