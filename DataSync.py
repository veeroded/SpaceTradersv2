import time
from Data import Agent, Fleet

import Data


def loop(Bearer):
    while True:
        Data.Agent(Bearer)
        Data.Fleet(Bearer)
        time.sleep(10)
