import pandas as pd
import matplotlib.pyplot as plt
import os

dataPath = "./Github/GameRecommendationSystem/data/"
dataName = "steamGames.csv"

def openCSV():
    columnsNames = ["userID","gameName","purchase","hours","delete"]
    df = pd.read_csv("C:/Users/Matheus/Desktop/Github/GameRecommendationSystem/data/steamGames.csv", names=columnsNames)
    return df.query("purchase == 'play'").drop(["purchase","delete"],axis = 1)

def treatDataset():
    df = filterDataset()
    nameGameUnique = df.index.unique()
    nameGameID = {Game:GameID for GameID,Game in zip(range(1,len(nameGameUnique)+1),nameGameUnique)}
    df = df.rename(index = nameGameID)
    return df, nameGameID

def filterDataset(mostPlayed = 0.2):
    df = openCSV()
    numberUniqueGames = len(df["gameName"].unique())
    selectedQuantity = int(numberUniqueGames*mostPlayed)
    gameSelect = df.groupby(["gameName"])["userID"].count().sort_values(ascending = False)[:selectedQuantity].keys()
    sparseMatrix = df.pivot_table(index='gameName',columns='userID',values='hours').fillna(0)
    return sparseMatrix.loc[gameSelect]