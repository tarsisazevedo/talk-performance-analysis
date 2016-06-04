import json
import requests
import logging

from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def perf():
    resp = requests.get("http://mtgjson.com/json/AllSetsArray.json")
    collections = resp.json()
    cards_name = []
    for collection in collections:
        for card in collection["cards"]:
            cards_name.append(card["name"])
    return json.dumps(cards_name)


if __name__ == '__main__':
    app.run("0.0.0.0", port=8888, processes=4)
