import json
import requests
import objgraph
# import logging

from flask import Flask, request
from memory_profiler import profile
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)
cache = SimpleCache()

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

@app.route("/")
@profile
def mem():
    collections = cache.get("mtg_coll")
    cards_name = []
    for collection in collections:
        for card in collection["cards"]:
            cards_name.append(card["name"])
    if request.args.get("measure"):
        objgraph.show_most_common_types()
    return json.dumps(cards_name)


if __name__ == '__main__':
    resp = requests.get("http://mtgjson.com/json/AllSetsArray.json")
    cache.set("mtg_coll", resp.json())
    app.run(processes=4)
