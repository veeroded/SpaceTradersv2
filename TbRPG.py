import os
import re


def MainMenu():
    print("""
    What Do you want to do 
    1.) Fleet
    2.) Contracts
    3.) Stop
    """)
    
    options = [Fleet() , Contracts(), Stop()]
    
    try :
        options[int(input(">"))]
    except IndexError:
        print("Refrain from being stupid")
        
def Fleet():
    

def Contracts():
    return "hi"

def Stop():
    if ConfirmationPrompt():
        os._exit(0)
    else:
        return

def ConfirmationPrompt():
    choice = input("Are you Sure y/n")
    if choice == "y":
        return True
    else:
        return False

CarryOn = True
FirstRun = input("Is this your first run of this program y/n")

if FirstRun == "y":
    if os.path.exists("./Data/"):
        os.makedirs("./Data/")
    Bearer = input("What is your Bearer")

    with open("./Token.txt", "w") as f:
        f.write(Bearer)

else:
    with open("./Token.txt" , "r") as f:
        bearer =

while CarryOn:
    MainMenu()
