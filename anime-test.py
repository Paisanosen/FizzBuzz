import requests
import json

    # to-do-list:
    # variables for type and status, not needed for now
    # sort list alphabetically or by highest anilist rating?
    # if 404 error on username, return error and reprompt

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
            }
            }
        }
    }
    }
    """
    variables = {
        "userName": anilistUsername,
        "type": "ANIME",
        "status": "COMPLETED"
    }
    url = "https://graphql.anilist.co"
    response = requests.post(url, json={"query": query, "variables": variables}) # HTTP request to server
    if response.status_code == 200:
        test_data_types(response)
    else:
        raise Exception(f"Error: {response.status_code}")

def test_data_types(response):
    if response.status_code == 200:

        userAnimeList = []
        animeListJson = json.dumps(response.json())
        animeList = json.loads(animeListJson)
        animeListData = animeList["data"]["MediaListCollection"]["lists"]
        
        # print(type(response)) # requests.models.Response
        # print(type(animeListJson)) # str
        # print(type(animeList)) # dict
        # print(type(animeListData))

        for data in animeListData:
            entries = data["entries"]
            # if English exists, add the English title, else add the romaji title
            for entry in entries:
                if entry["media"]["title"]["english"] != None:
                    animeTitle = entry["media"]["title"]["english"]
                    userAnimeList.append(animeTitle)
                else:
                    animeTitle = entry["media"]["title"]["romaji"]
                    userAnimeList.append(animeTitle)
        for i in sorted(userAnimeList, key=str.casefold):
            print(i)
    else:
        raise Exception(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()