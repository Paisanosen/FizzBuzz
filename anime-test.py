import requests
import json

    # problems:
    # cannot pass userinput variable into the query
    # cannot iterate for loop of json response to read each anime title
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
    #-------------------------------------------------------------------------------------------#
    # HTTP request to server
    response = requests.post(url, json={"query": query, "variables": variables})
    if response.status_code == 200:
        # print(json.dumps(response.json(), indent=2))
        test_data_types(response)

            # print(data["data"]["MediaListCollection"]["lists"])
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
        # print(animeList["data"]["MediaListCollection"]["lists"]) # trying to access the next key in the dictionary (entries) returns typeerror
        animeListData = animeList["data"]["MediaListCollection"]["lists"]
        print(type(animeListData))
        for data in animeListData:
            # print(data)
            print(type(data))
            entries = data["entries"]
            # print(entries)
            print(type(entries))
            for entry in entries:
                # print(entry)
                # print(type(entry))
                animeTitle = entry["media"]["title"]["romaji"]
                print(animeTitle)
    else:
        raise Exception(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()