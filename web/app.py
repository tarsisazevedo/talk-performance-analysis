import json
import requests

from flask import Flask

app = Flask(__name__)

@app.route("/")
@profile
def index():
    resp = requests.get("http://mtgjson.com/json/AllSetsArray.json")
    collections = resp.json()
    cards_name = []
    for collection in collections:
        for card in collection["cards"]:
            cards_name.append(card["name"])
    return json.dumps(cards_name)


if __name__ == '__main__':
    app.run()
