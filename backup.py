# Import all the things needed for the program to funtion
import time
import os
import random
import pyfiglet
import sys

# Define the scores so they wont be overwriten
playerScore = 0
computerScore = 0


# Clear the screen
# Operting system detection funciton from stack overflow modifed.
# https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python

def screenClear():
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system('clear')
    elif sys.platform == "darwin":
        os.system('clear')
    elif sys.platform == "win32":
        os.system('cls')


# Display Welcome Message
def welcomeMessage():
    print(pyfiglet.figlet_format("Welcome to King of the Jungle."))
    time.sleep(0)
    screenClear()


# Display thr rule screen
def rulesScreen():
	print("""The rules of this game are:
 1. You will be asked to pick an animal.
 2. The computer will then pick randomly one of the 3 animals.
 3. If you can the computer both pick the same animal,
 a message will be displayed saying no battle was fought
 4. If it is not tied the winner will be decide with these combat rules:
    Lion beats mouse
    Mouse beats Elephant
    Elephant beats lion
 5. The winner will be displayed and given a point.
 6. Pressing 0 will display the score and exit.
 """)
input("Press the enter key to continue to the menu: ")
screenClear()


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
		print("Heres the scoreboard")
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
	computerAnimalNumb = 0
	computerAnimal = ""
	computerAnimalNumb = (random.randint(1,3))
	# Make the computers choice a animal name rather than a number to make it easier to keep track of. This will probaly be removed and just used as a number.
	if computerAnimalNumb == 1:
		computerAnimal = "lion"
	elif computerAnimalNumb == 2:
		computerAnimal = "elephant"
	elif computerAnimalNumb == 3:
		computerAnimal = "mouse"

	return computerAnimal


def mainGame(playerAnimal, computerAnimal, playerScore, computerScore):
	if playerAnimal == computerAnimal:
		print("Draw no battle was forght, both players picked the same animal.")
	elif playerAnimal == "lion":
		if computerAnimal == "mouse":
			print("You Win the computer chose mouse and lion beats mouse.")
			playerScore += 1
			
		else:
			print("You loose computer elphant beats lion")
			computerScore += 1
	elif playerAnimal == "mouse":
		if computerAnimal == "elephant":
			print("You win the computer chose elephant and mouse beats elephant.")
			playerScore += 1
		else:
			print("You loose the computer chose lion which beats mouse.")
			computerScore += 1
	elif playerAnimal == "elephant":
		if computerAnimal == "lion":
			print("you win the computer chose lion and elaphant beats lion or something")
			playerScore += 1
		else:
			print("You loose computer chose mouse and mouse beats elephant")
			computerScore += 1

	input("Press enter to goto the main menu")
	playerAnimal, computerAnimal = "", ""
	return playerAnimal, computerAnimal

def scoreBoard(playerScore , computerScore):
	print("Welcome to the scoreboard as it stands the score currently is:")
	if playerScore > computerScore:
		print("The player is winning and computer is loosing")
		print("The score is {} for the player and {} for the computer".format(playerScore, computerScore))
	elif playerScore == computerScore:
		print("The score is tied with both the computer and the player tied")
		print("The score is {} for both players".format(playerScore))
	elif playerScore < computerScore:
		print("The computer is winning and the players is loosing")
		print("The score is {} for the computer and {} for tge player".format(computerScore, playerScore))
	quit = True
	

	return quit
welcomeMessage()
rulesScreen()


while True:
	if quit == True:
		break
	else:
		playerAnimal, computerAnimal = menu()
		playerAnimal, computerAnimal = mainGame(playerAnimal, computerAnimal, playerScore, computerScore)
