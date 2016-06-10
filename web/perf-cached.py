import json
import requests
import logging

from flask import Flask, request
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)
app.debug=True

cache = SimpleCache()
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def perf():
    collections = cache.get("mtg_coll")
    cards_name = []
    for collection in collections:
        for card in collection["cards"]:
            cards_name.append(card["name"])
    return json.dumps(cards_name)


if __name__ == '__main__':
    resp = requests.get("http://mtgjson.com/json/AllSetsArray.json")
    cache.set("mtg_coll", resp.json())
    app.run("0.0.0.0", port=8888, processes=4)
