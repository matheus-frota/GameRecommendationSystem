from knnRecommender import knn

def main():
    k = int(input("Quantos jogos você quer que lhe recomendamos? "))
    gameName = input("Digite o nome do seu jogo favorito: ")

    knn.recommender(k,gameName)