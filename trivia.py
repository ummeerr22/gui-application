import requests
from pprint import pprint
import json

url = "https://opentdb.com/api.php?amount=50&category=9"

response = requests.get(url)
pprint(response)
pprint(response.json())
with open("trivia.json", "w") as f:
    json.dump(response.json(), f, indent=4)