import random

def main():
    animeList = ["Honey and Clover", "Hinamatsuri", "Ping Pong the Animation", "White Album 2"]
    random.shuffle(animeList)

    n = len(animeList)
    print(n)
    for i in range(n-1):
        for j in range(0, (n - i - 1)):
            message = animeList[j] + " or " + animeList[j + 1] + "\n"
            userChoice = input(message).upper()
            if userChoice == "L":
                animeList[j], animeList[j + 1] = animeList[j + 1], animeList[j]
            elif userChoice == "R":
                pass
    # show top anime at the top rather than bottom
    animeList.reverse()
    for i in range(len(animeList)):
        print(animeList[i])

if __name__ == "__main__":
    main()