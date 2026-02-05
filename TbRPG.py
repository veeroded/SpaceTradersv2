import os
from functools import partial


def MainMenu():
    print("""
    What Do you want to do
    1.) Fleet
    2.) Contracts
    0.) Stop
    """)

    Selector([partial(Stop), partial(Fleet), partial(Contracts)])


def Selector(options):
    try:
        options[int(input(">"))]()
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


FirstRun = input("Is this your first run of this program y/n :")

if (FirstRun == "y") and (ConfirmationPrompt()):
    if os.path.exists("./Data/"):
        os.makedirs("./Data/")
    Bearer = input("What is your Bearer")

    with open("./Token.txt", "w") as f:
        f.write(Bearer)

else:
    with open("Token.txt", "r") as f:
        Bearer = f.read().replace("\n", "")

MainMenu()
