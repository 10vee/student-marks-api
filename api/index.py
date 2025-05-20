import json
import os

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    if request.method != "GET":
        response.status_code = 405
        return response.send("Method Not Allowed")

    # Correct path to marks.json
    json_path = os.path.join(os.path.dirname(__file__), "..", "marks.json")
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        response.status_code = 500
        return response.send("marks.json not found")

    names = request.query.get("name", [])
    if isinstance(names, str):
        names = [names]

    marks = [data.get(name, None) for name in names]
    return response.json({"marks": marks})
