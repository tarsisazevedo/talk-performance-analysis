import json
import requests

from memory_profiler import profile
from flask import Flask

app = Flask(__name__)


@profile
@app.route("/mem")
def mem():
    resp = requests.get("http://mtgjson.com/json/AllSetsArray.json")
    collections = resp.json()
    cards_name = []
    for collection in collections:
        for card in collection["cards"]:
            cards_name.append(card["name"])
    return json.dumps(cards_name)


if __name__ == '__main__':
    app.run()

