import requests
import json

    # problems:
    # cannot pass userinput variable into the query
    # anilistName = input("Enter your AniList username: ")
    # anilistType = "ANIME"
    # anilistStatus = "COMPLETED"
    # would like list to use 3 variables for the MediaListCollection query instead of hardcoding

def main():
    #-------------------------------------------------------------------------------------------#
    query = """
    query {
    MediaListCollection(userName: "Meltiply", type: ANIME, status: COMPLETED) {
        lists {
            entries {
            media {
                title {
                romaji
                english
                }
            }
            }
        }
    }
    }
    """
    variables = {
        "userName": "Meltiply",
        "type": "ANIME",
        "status": "COMPLETED"
    }
    url = "https://graphql.anilist.co"
    response = requests.post(url, json={"query": query, "variables": variables}) # HTTP request to server
    if response.status_code == 200:
        test_data_types(response)
    else:
        raise Exception(f"Error: {response.status_code}")
    #-------------------------------------------------------------------------------------------#

def test_data_types(response):
    if response.status_code == 200:
        userAnimeList = []
        print(type(response)) # requests.models.Response
        animeListJson = json.dumps(response.json())
        print(type(animeListJson)) # str
        animeList = json.loads(animeListJson)
        print(type(animeList)) # dict
        animeListData = animeList["data"]["MediaListCollection"]["lists"]
        print(type(animeListData))
        for data in animeListData:
            entries = data["entries"]
            for entry in entries:
                if entry["media"]["title"]["english"] != None:
                    animeTitle = entry["media"]["title"]["english"]
                    userAnimeList.append(animeTitle)
                else:
                    animeTitle = entry["media"]["title"]["romaji"]
                    userAnimeList.append(animeTitle)
        for i in userAnimeList:
            print(i)
    else:
        raise Exception(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()