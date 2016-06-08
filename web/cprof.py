import json
import requests

from flask import Flask, request
from werkzeug.contrib.profiler import ProfilerMiddleware

app = Flask(__name__)
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir="profile")
app.debug = True


@app.route("/")
def cprof():
    resp = requests.get("http://mtgjson.com/json/AllSetsArray.json")
    collections = resp.json()
    cards_name = []
    for collection in collections:
        for card in collection["cards"]:
            cards_name.append(card["name"])
    return json.dumps(cards_name)


if __name__ == '__main__':
    app.run('0.0.0.0', processes=4)
