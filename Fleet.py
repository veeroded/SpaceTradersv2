import json
from requests import get, post, patch
from Data import Ships


def Listships():
    with open("./Data/Ships.json", "r") as f:
        data = json.load(f)
    values = []
    for i in data[0]["data"]:
        values.append(
            {
                "Symbol": i["symbol"],
                "role": i["registration"]["role"],
                "Waypoint": i["nav"]["waypointSymbol"],
            }
        )
    return values


print(Listships())
