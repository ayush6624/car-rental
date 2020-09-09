import requests
import json


url = "https://api.zoomcar.com/v4/airport_terminals?platform=web"
data = requests.get(url).json()
data = data['terminals']
for i in data:
    with open("{}.json".format(i['city']), "w") as f:
        json.dump(i, f)
