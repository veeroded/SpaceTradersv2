from requests import get, post
import json

with open("Token.txt", "r") as f:
    Bearer = f.read()


def Agent(Bearer):
    f = open("./Data/Agent.json", "w")
    json.dump(
        get(
            "https://api.spacetraders.io/v2/my/agent",
            headers={"Authorization": f"Bearer {Bearer}"},
        ).json(),
        f,
    )


def Systems(Bearer):
    f = open("./Data/Systems.json", "w")
    json.dump(
        get(
            "https://api.spacetraders.io/v2/systems",
            headers={"Authorization": f"Bearer {Bearer}"},
        ).json(),
        f,
    )


print(Bearer)
# Systems(Bearer)
