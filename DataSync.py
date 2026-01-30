import time
from Data import Agent, Fleet

import Data

with open("Token.txt", "r") as f:
    Bearer = f.read().replace("\n", "")


def loop(Bearer):
    while True:
        Data.Agent(Bearer)
        Data.Fleet(Bearer)
        time.sleep(30)


loop(Bearer)
