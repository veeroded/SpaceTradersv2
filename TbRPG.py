import os
from threading import Thread
from functools import partial
from DataSync import loop


def MainMenu():
    while True:
        print("""
What Do you want to do
1.) Fleet
2.) Contracts
0.) Stop
        """)

        Selector([partial(Stop), partial(Fleet), partial(Contracts)])


def Selector(options):
    try:
        user_input = int(input(">"))
        return options[user_input]()
    except IndexError:
        ("Refrain from being stupid")


def Fleet():
    print("""
What Do you want to do 
1.) Current Ships 
2.) Buy Ships
0.) Back
    """)

    if Selector([lambda: "Back"]) == "Back":
        return
    else:
        pass


def Contracts():
    print("hi")


def Stop():
    if ConfirmationPrompt():
        os._exit(0)
    else:
        return


def ConfirmationPrompt():
    choice = input("Are you Sure y/n: ")
    if choice == "y":
        return True
    else:
        return False


FirstRun = input("Is this your first run of this program y/n :").strip().lower()

if FirstRun == "y":
    Bearer = input("What is your Bearer\n")
    with open("./Token.txt", "w") as f:
        f.write(Bearer)
    if not (os.path.exists("./Data/")):
        os.makedirs("./Data/")

else:
    with open("Token.txt", "r") as f:
        Bearer = f.read().replace("\n", "")

LoopThread = Thread(target=loop, args=(Bearer,))
LoopThread.start()

MainMenu()
