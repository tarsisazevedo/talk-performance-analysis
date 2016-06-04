import json
import requests
import logging

from flask import Flask, request
from werkzeug.contrib.cache import RedisCache

app = Flask(__name__)
app.debug=True

cache = RedisCache(host="192.168.0.101", port=6379)
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

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
