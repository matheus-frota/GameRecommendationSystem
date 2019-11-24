#import pandas as pd
#import databaseOrganization as do
from knnRecommender.databaseOrganization import treatDataset
import numpy
from knnRecommender.utilits import cosineSimilarity, sortValueDict, similarNames

def train(data, gameNameData):
    distanceGames = {}
    gameNameX = data[data.index == gameNameData].values
    gameNameX = numpy.asarray(gameNameX).ravel()
    for index,gameNameY in data.iterrows():
        distanceGames[index] = cosineSimilarity(gameNameX,gameNameY.values)
    return sortValueDict(distanceGames)

def recommender(k, gameNameUser):
    data, nameGameID = treatDataset()
    trainData, testData = trainTestSplit(data)
    gamesNameData = similarNames(gameNameUser, nameGameID)
    if gamesNameData == None:
        print("Nenhum jogo com esse nome foi encontrado!")
    else:
        gamesRecommender = train(trainData,gamesNameData)
        replaceID = {ID:name for name,ID in zip(nameGameID.keys(),nameGameID.values())}
        print("-----Recomendações-----\n")
        for game in gamesRecommender[1:k+1]:
            amountPlayersGames = validation(game[0],gamesNameData,testData)
            print("{} - {} usuário(s) possuem ambos os jogos!".format(replaceID[game[0]],amountPlayersGames))

def trainTestSplit(data, split = 0.4):
    numberColumns = len(data.columns)
    columnsPermutation = numpy.random.permutation(numberColumns)
    trainColumns = columnsPermutation[int(numberColumns*split):]
    testColumns = columnsPermutation[:int(numberColumns*split)]
    return data.iloc[:,trainColumns],data.iloc[:,testColumns]

def validation(nameGameRecommender, nameGameUser, testData):
    validationData = testData.loc[[nameGameUser,nameGameRecommender],:].copy()
    validationDataTranspose = validationData.T
    userFilterWithBothGames = validationDataTranspose[(validationDataTranspose[nameGameUser] != 0) & (validationDataTranspose[nameGameRecommender] != 0)]
    return userFilterWithBothGames.shape[0]