import os
from threading import Thread
from functools import partial
from DataSync import loop
from Fleet import Listships


def MenuSelector(options):
    try:
        user_input = int(input(">"))
        return options[user_input]()
    except IndexError:
        print("Refrain from being stupid (INDEX)")
        return
    except ValueError:
        print("Refrain from being stupid (VALUE)")
        return


# MainMenu
def MainMenu():
    while True:
        print("""
What Do you want to do
1.) Fleet
2.) Contracts
0.) Stop
        """)

        MenuSelector([partial(Stop), partial(Listships), partial(Contracts)])


##Fleet


def FleetMenu():
    print("""
What Do you want to do 
1.) Current Ships 
2.) Buy Ships
0.) Back
    """)

    MenuSelector([lambda: "Back", partial(CurrentShips)])


###
def CurrentShips():
    a = Listships()


##Contracts
def Contracts():
    print("hi")


##Stop
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
