import json
import os

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    if request.method != "GET":
        response.status_code = 405
        return response.send("Method Not Allowed")

    # Resolve the correct path to marks.json
    json_path = os.path.join(os.path.dirname(__file__), "..", "marks.json")
    with open(json_path, "r") as f:
        data = json.load(f)

    names = request.query.get("name", [])
    if isinstance(names, str):
        names = [names]

    marks = [data.get(name, None) for name in names]
    return response.json({"marks": marks})
