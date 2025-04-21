import requests
import json

print("Search Song In Itunes Apple")
artist = input("Artist: ")
try:
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1", {"term": artist}
    )  #Itunes apple API
    response.raise_for_status()
except requests.HTTPError:          #Error 404, Error 500, Connection problem, etc
    print("Cant complated request")
    exit()

print (json.dumps(response.json(), indent=2))