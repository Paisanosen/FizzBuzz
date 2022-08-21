import requests
import json
import random

    # to-do-list:
    # variables for type and status, not needed for now
    # if 404 error on username, return error and reprompt
    # add error checking everywhere
    # implement a different comparison method
    # allow the user to skip an entry and come back to it later
    # bubble method sort will pin the same anime against each other multiple times, want to avoid this
    # divide parts of code into separate, distinct functions
    # deploy as webapp with django
    # save iterations by default sorting by anilist rating
    # sort initial array by average score

def main():
    #-------------------------------------------------------------------------------------------#
    anilistUsername = input("Enter your AniList username: ")
    query = """
    query($userName: String) {
        MediaListCollection(userName: $userName, type: ANIME, status: COMPLETED) {
            lists {
                entries {
                media {
                    title {
                    romaji
                    english
                        }
                    averageScore
                    }
                }
            }
        }
    }
    """
    variables = {
        "userName": anilistUsername,
        "type": "ANIME",
        "status": "REPEATING"
    }
    url = "https://graphql.anilist.co"
    response = requests.post(url, json={"query": query, "variables": variables}) # HTTP request to server
    if response.status_code == 200:
        test_data_types(response)
    else:
        raise Exception(f"Error: {response.status_code}")

def test_data_types(response):

    userAnimeList = []
    userAnimeListScores = []

    if response.status_code == 200:

        animeListJson = json.dumps(response.json()) # convert requests.models.Response to str
        animeList = json.loads(animeListJson) # convert str to dict
        animeListData = animeList["data"]["MediaListCollection"]["lists"]

        for data in animeListData:
            entries = data["entries"]
            # if English exists, add the English title, else add the romaji title
            for entry in entries:
                # append anime scores to different array
                animeTitleScore = entry["media"]["averageScore"]
                userAnimeListScores.append(animeTitleScore)
                if entry["media"]["title"]["english"] != None:
                    animeTitle = entry["media"]["title"]["english"]
                    userAnimeList.append(animeTitle)
                else:
                    animeTitle = entry["media"]["title"]["romaji"]
                    userAnimeList.append(animeTitle)
        # for i in sorted(userAnimeList, key=str.casefold):
        #     print(i)
    else:
        raise Exception(f"Error: {response.status_code}")

    # -------------------------------------------------------------------
    random.shuffle(animeList)

    n = len(userAnimeList)
    print(n)
    # for i in range(n-1):
    #     for j in range(0, (n - i - 1)):
    #         message = userAnimeList[j] + " or " + userAnimeList[j + 1] + "\n"
    #         # userChoice = input(message).upper()
    #         userChoice = random.randint(0, 1)
    #         if userChoice == "L":
    #             userAnimeList[j], userAnimeList[j + 1] = userAnimeList[j + 1], userAnimeList[j]
    #         elif userChoice == "R":
    #             pass
    # show top anime at the top rather than bottom
    # userAnimeList.reverse()
    for i in range(len(userAnimeList)):
        print(userAnimeList[i])
        print(userAnimeListScores[i])
    
if __name__ == "__main__":
    main()