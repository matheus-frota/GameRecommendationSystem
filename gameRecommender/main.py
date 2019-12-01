from knn import recommender

def main():
    k = int(input("Quantos jogos você quer que lhe recomendamos? "))
    gameName = input("Digite o nome do seu jogo favorito: ")

    recommender(k,gameName)

main()