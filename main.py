# Import all the things needed for the program to funtion
import time
import os
import random
import pyfiglet
import sys
import utils

# Define the scores so they wont be overwriten
playerScore = 0
computerScore = 0


# Display Welcome Message
def welcomeMessage():
    print(pyfiglet.figlet_format("Welcome to King of the Jungle."))
    time.sleep(3)
    utils.screenClear()


def menu():
    print("Welcome to the king of the Jungle:")
    print("Please select an animal or exit.")
    print("""Your Choices are:
        1) Lion
        2) Elephant
        3) Mouse
        0) Exit and view the score""")
    playerAnimalNumb = ""
    playerAnimal = ""
    while playerAnimalNumb not in ['0', '1', '2', '3']:
        playerAnimalNumb = str.upper(input("Your selection: "))
    if playerAnimalNumb == "0":
        print("Thanks for playing")
        print("This is the scoreboard")
        scoreBoard(playerScore, computerScore)
    elif playerAnimalNumb == "1":
        playerAnimal = "lion"
    elif playerAnimalNumb == "2":
        playerAnimal = "elephant"
    elif playerAnimalNumb == "3":
        playerAnimal = "mouse"
    computerAnimal = computerAnimalGenerator()
    return playerAnimal, computerAnimal


def computerAnimalGenerator():
    computerAnimalChoices = ["lion", "elephant", "mouse"]
    computerAnimal = random.choice(computerAnimalChoices)
    return computerAnimal


def mainGame(playerAnimal, computerAnimal, playerScore, computerScore):
    if playerAnimal == computerAnimal:
        print("Argh, there was no battle you both chose {}.".format(playerAnimal))
    elif playerAnimal == "lion":
        if computerAnimal == "mouse":
            print("Argh, you won lion beats mouse you are the king this time!")
            playerScore += 1
        else:
            print("Argh, you lost this one elephant beats lion!")
            computerScore += 1
    elif playerAnimal == "mouse":
        if computerAnimal == "elephant":
            print(
                "Argh, you won this time mouse beats elephant, this time your the king!"
            )
            playerScore += 1
        else:
            print("Argh, you lost this time lion beats up poor mouse!.")
            computerScore += 1
    elif playerAnimal == "elephant":
        if computerAnimal == "lion":
            print("Argh, you win this one elephant beats ")
            playerScore += 1
        else:
            print("You loose computer chose mouse and mouse beats elephant")
            computerScore += 1

    input("Press enter to goto the main menu")
    utils.screenClear()
    playerAnimal, computerAnimal = "", ""
    return playerAnimal, computerAnimal


def scoreBoard(playerScore, computerScore):
    print("Welcome to the scoreboard as it stands the score currently is:")
    if playerScore > computerScore:
        print("The player is winning and computer is loosing")
        print("The score is {} for the player and {} for the computer".format(
            playerScore, computerScore))
    elif playerScore == computerScore:
        print("The score is tied with both the computer and the player tied")
        print("The score is {} for both players".format(playerScore))
    elif playerScore < computerScore:
        print("The computer is winning and the players is loosing")
        print("The score is {} for the computer and {} for tge player".format(
            computerScore, playerScore))
    exit()


welcomeMessage()
utils.rulesScreen()

while True:
    playerAnimal, computerAnimal = menu()
    playerAnimal, computerAnimal = mainGame(
        playerAnimal, computerAnimal, playerScore, computerScore
    )
