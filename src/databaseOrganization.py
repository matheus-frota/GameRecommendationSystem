import pandas as pd

def openCSV():
    columnsNames = ["userID","nameGame","purchase","hours","delete"]
    df = pd.read_csv("C:/Users/Matheus/Desktop/Github/GameRecommendationSystem/data/steamGames.csv", names=columnsNames)
    print(df.head())

openCSV()
