from requests import get, post
import json

with open("Token.txt", "r") as f:
    Bearer = f.read()

def JsonDump(int Bearer,str item, file)
    with open(f"./Data/{file}", "w0"):
        json.dump(
            json.loads(get(
                f"https://api.spacetraders.io/v2/{item}",
                headers={"Authorization": f"Bearer {Bearer}"},
            ).text),
            f,
            indent = 4
        )
        


def Agent(Bearer):
    f = open("./Data/Agent.json", "w")
    json.dump(
        json.loads(get(
            "https://api.spacetraders.io/v2/my/agent",
            headers={"Authorization": f"Bearer {Bearer}"},
        ).text),
        f,
        indent = 4
    )


def Systems(Bearer):
    f = open("./Data/Systems.json", "w")
    json.dump(
        json.loads(get(
            "https://api.spacetraders.io/v2/systems",
            headers={"Authorization": f"Bearer {Bearer}"},
        ).text),
        f,
        indent = 4
    )
    
def TradeRelations(Bearer):
        f = open("./Data/Systems.json", "w")
    json.dump(
        json.loads(get(
            "https://api.spacetraders.io/v2/systems",
            headers={"Authorization": f"Bearer {Bearer}"},
        ).text),
        f,
        indent = 4
    )
    
Systems(Bearer)
Agent(Bearer)