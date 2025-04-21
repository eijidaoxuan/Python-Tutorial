import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=all&term={sys.argv[1]}").json()
print (response["results"][0]["trackName"])
for result in response["results"]:
    print(result["trackName"])
