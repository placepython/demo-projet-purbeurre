import json
from pprint import pprint

with open("mesdonnee.json") as json_file:
    data = json.load(json_file)

pprint(data)
