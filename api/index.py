

import json
import os

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    if request.method != "GET":
        response.status_code = 405
        return response.send("Method Not Allowed")

    with open(os.path.join(os.path.dirname(__file__), "../marks.json")) as f:
        data = json.load(f)

    names = request.query.get("name", [])
    if isinstance(names, str):
        names = [names]

    marks = [data.get(name, None) for name in names]
    return response.json({"marks": marks})
