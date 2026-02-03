from requests import post
import json

with open("Token.txt", "r") as f:
    Bearer = f.read().replace("\n", "")


def ReturnKey(Bearer):
    with open("./Data/Contracts.json", "r") as f:
        Contracts = json.loads(f.read())
    return Contracts


print(ReturnKey(Bearer))
