import time
from Data import Agent, Ships

with open("Token.txt", "r") as f:
    Bearer = f.read().replace("\n", "")


def loop(Bearer):
    while True:
        Agent(Bearer)
        Ships(Bearer)
        time.sleep(10)
