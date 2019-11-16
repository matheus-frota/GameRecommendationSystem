import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

dataPath = "./Github/GameRecommendationSystem/data/"
dataName = "steamGames.csv"

def openCSV():
    columnsNames = ["userID","gameName","purchase","hours","delete"]
    gamesDataBase = pd.read_csv("C:/Users/Matheus/Desktop/Github/GameRecommendationSystem/data/steamGames.csv", names=columnsNames)
    return gamesDataBase.query("purchase == 'play'").drop(["purchase","delete"],axis = 1)

def treatDataset():
    sparseMatrixGamesDataBase = filterDataset()
    nameGameUnique = sparseMatrixGamesDataBase.index.unique()
    nameGameID = {Game:GameID for GameID,Game in zip(range(1,len(nameGameUnique)+1),nameGameUnique)}
    sparseMatrixGamesDataBase = sparseMatrixGamesDataBase.rename(index = nameGameID)
    return sparseMatrixGamesDataBase, nameGameID

def filterDataset(mostPlayed = 0.2):
    gamesDataBase = openCSV()
    numberUniqueGames = len(gamesDataBase["gameName"].unique())
    selectedQuantity = int(numberUniqueGames*mostPlayed)
    gameSelect = gamesDataBase.groupby(["gameName"])["userID"].count().sort_values(ascending = False)[:selectedQuantity].keys()
    sparseMatrix = gamesDataBase.pivot_table(index='gameName',columns='userID',values='hours').fillna(0)
    return sparseMatrix.loc[gameSelect]