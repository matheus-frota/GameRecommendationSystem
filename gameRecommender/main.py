from knn import recommender, personalization

def main():
    k = int(input("How many games do you want to know? "))
    gameName = input("Enter the name of your favorite game: ")
    personalization()
    recommender(k,gameName)

main()