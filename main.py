from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hardcoded marks data (paste your full JSON here)
marks_data = {"name":"beM7BNhKE","marks":24},{"name":"jH52eNkHE","marks":65},{"name":"mDHF9H2zD","marks":75},{"name":"r6I8mmbHCS","marks":19},{"name":"vkFC","marks":59},{"name":"eJjc1a9zq","marks":51},{"name":"RW","marks":11},{"name":"d","marks":80},{"name":"xrb1uPxQ","marks":40},{"name":"JuWPO","marks":90},{"name":"rdARVw","marks":60},{"name":"LhGkmxhpQ","marks":91},{"name":"oCxTNsed","marks":71},{"name":"P","marks":33},{"name":"m","marks":99},{"name":"pF3BEQRP","marks":63},{"name":"o2AAxBSOHc","marks":11},{"name":"Zbrf","marks":34},{"name":"v5GwKVYuCA","marks":41},{"name":"k","marks":14},{"name":"KZj","marks":24},{"name":"9UbYD","marks":4},{"name":"QSSqBy","marks":14},{"name":"a3hwY4k02","marks":28},{"name":"zQr","marks":70},{"name":"dVf","marks":78},{"name":"tQlakap4","marks":32},{"name":"drQD","marks":51},{"name":"Oqt","marks":18},{"name":"zLmlAaS","marks":43},{"name":"n","marks":45},{"name":"fXkuwo","marks":23},{"name":"sm","marks":55},{"name":"evTq","marks":57},{"name":"WCLQF0Y","marks":86},{"name":"fDDfjcJXJY","marks":44},{"name":"EQqMlxD6","marks":51},{"name":"ZhJeYca7","marks":44},{"name":"EFMUQG8","marks":65},{"name":"X9id7vw9Ay","marks":31},{"name":"D6ldJqcj","marks":88},{"name":"cjvyT6fWU","marks":42},{"name":"i0LCd","marks":80},{"name":"vzYVHWfPnk","marks":64},{"name":"OVwjRyd","marks":53},{"name":"tFO9dNH","marks":14},{"name":"pct7wb0L","marks":89},{"name":"UzX3C","marks":16},{"name":"X8AR0VesWR","marks":66},{"name":"R0M1SnmZ","marks":18},{"name":"oVUsDw7","marks":83},{"name":"BagpF","marks":92},{"name":"vyvlp","marks":50},{"name":"IgTqDD","marks":63},{"name":"sODlzXflS","marks":96},{"name":"x","marks":80},{"name":"wSq3sXOE","marks":3},{"name":"p70TLG","marks":76},{"name":"RF40d931H","marks":28},{"name":"kAP3","marks":97},{"name":"AhIQW5tCTn","marks":59},{"name":"Is","marks":56},{"name":"A9nXJtSw","marks":77},{"name":"kA5Vl","marks":3},{"name":"t0QYc","marks":41},{"name":"EPMzgHyB","marks":60},{"name":"x7Sf","marks":20},{"name":"u","marks":78},{"name":"XdSfu2Bb","marks":99},{"name":"cdkIIBY","marks":53},{"name":"71azF","marks":38},{"name":"VeafJOE","marks":71},{"name":"KiM8qABpS","marks":95},{"name":"rLZn","marks":76},{"name":"iNC3","marks":16},{"name":"cpT69B","marks":88},{"name":"RRL53","marks":96},{"name":"pjE6X6ojBI","marks":54},{"name":"nRE8","marks":17},{"name":"U","marks":59},{"name":"swaOwy","marks":33},{"name":"G2G8ay8S6","marks":72},{"name":"np","marks":28},{"name":"CzNhl16kUN","marks":64},{"name":"bPrgfkA","marks":70},{"name":"p9aKF5K","marks":48},{"name":"1UDe","marks":58},{"name":"BJKD","marks":37},{"name":"VvDcW","marks":58},{"name":"1FrxxFrV","marks":43},{"name":"KL","marks":27},{"name":"ruKZ0DI","marks":6},{"name":"aIzr0XR","marks":18},{"name":"pnnLwP9Q","marks":24},{"name":"wimpQ","marks":80},{"name":"2","marks":79},{"name":"xjhYTrM","marks":39},{"name":"6pEreGeXKL","marks":38},{"name":"bEyAy6xR","marks":93},{"name":"Dg7qL","marks":7}


@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
