from requests import get, post
import json

with open("Token.txt", "r") as f:
    Bearer = f.read().replace("\n", "")


def JsonDump(Bearer, item, file):
    with open(f"./Data/{file}", "w") as f:
        json.dump(
            json.loads(
                get(
                    f"https://api.spacetraders.io/v2/{item}",
                    headers={"Authorization": f"Bearer {Bearer}"},
                ).text
            ),
            f,
            indent=4,
        )


def Agent(Bearer):
    JsonDump(Bearer, "my/agent", "Agent.json")


def Systems(Bearer):
    JsonDump(Bearer, "/systems", "Systems.json")


def Fleet(Bearer):
    JsonDump(Bearer, "/my/ships", "Ships.json")


Agent(Bearer)
Fleet(Bearer)
