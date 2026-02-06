import time
from Data import Agent, Ships

import Data

with open("Token.txt", "r") as f:
    Bearer = f.read().replace("\n", "")


def loop(Bearer):
    while True:
        Data.Agent(Bearer)
        Data.Ships(Bearer)
        time.sleep(10)
