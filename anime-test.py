import requests
import json


def main():
    # problems:
    # cannot pass userinput variable into the query
    # cannot iterate for loop of json response to read each anime title
    # anilistName = input("Enter your AniList username: ")
    # anilistType = "ANIME"
    # anilistStatus = "COMPLETED"
    # would list to use 3 variables for the MediaListCollection query instead of hardcoding

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

    # HTTP request to server
    response = requests.post(url, json={"query": query, "variables": variables})
    if response.status_code == 200:
        # print(json.dumps(response.json(), indent=2))
        # convert string to Python dictionary
        print(type(response)) # requests.models.Response
        animeListJson = json.dumps(response.json())
        print(type(animeListJson)) # str
        animeList = json.loads(animeListJson)
        print(type(animeList)) # dict
        # need to print only romaji titles
        # trying to access the next key in the dictionary (entries) returns typeerror
        print(animeList["data"]["MediaListCollection"]["lists"])
        # print(type(animeList)) # dict
        # print(animeList["data"]["MediaListCollection"].keys())
        # animeList = json.loads(animeListJson)

        # data = response.json()
        # print(data)
        # print(type(data)) # dict
        # print(response.keys())
    else:
        raise Exception(f"Error: {response.status_code}")


    # print(json.dumps(response.json(), indent=2))
    # response["MediaListCollection"]["lists"]["entries"]["media"]["title"]["romaji"]
        
if __name__ == "__main__":
    main()

# # Here we define our query as a multi-line string
# query = '''
# query ($id: Int) { # Define which variables will be used in the query (id)
#   Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
#     id
#     title {
#       romaji
#       english
#       native
#     }
#   }
# }
# '''

# # Define our query variables and values that will be used in the query request
# variables = {
#     'id': 15125
# }

# url = 'https://graphql.anilist.co'

# # Make the HTTP Api request
# response = requests.post(url, json={'query': query, 'variables': variables})

# print(response.status_code)
# print(json.dumps(response.json(), indent=2))