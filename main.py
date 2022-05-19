# Import all the things needed for the program to funtion
import random
import utils

# Define the scores so they wont be overwriten
playerScore = 0
computerScore = 0


# Main menu function for game this is where most things happen.
def menu(playerScore, computerScore):
    # Interface so the user knows whats going on.
    print("Welcome to the king of the Jungle:")
    print("Please select an animal or exit.")
    print("""Your Choices are:
        1) Lion
        2) Elephant
        3) Mouse
        0) Exit and view the score""")

    # Reset the varibles for the players animals so it wont cause issues.
    playerAnimalNumb = ""
    playerAnimal = ""

    # Get the users imput and make sure its vaild.
    while playerAnimalNumb not in ['0', '1', '2', '3']:
        playerAnimalNumb = str.upper(input("Your selection: "))

    # Handle if the user wants to quit the program
    if playerAnimalNumb == "0":
        if playerScore == 0 and computerScore == 0:
            utils.screenClear()
            print("Thanks for playing and goodbye")
            print("There is no need to see the score since no one has scored")
            exit()
        print("Thanks for playing")
        print("This is the scoreboard")
        scoreBoard(playerScore, computerScore)
    # Convert the number imput into a word so it is easier to understand
    elif playerAnimalNumb == "1":
        playerAnimal = "lion"
    elif playerAnimalNumb == "2":
        playerAnimal = "elephant"
    elif playerAnimalNumb == "3":
        playerAnimal = "mouse"

    # Run the function to get the computers animal choice
    computerAnimal = computerAnimalGenerator()

    return playerAnimal, computerAnimal


# Generate the computers animal choice from a list.
def computerAnimalGenerator():
    computerAnimalChoices = ["lion", "elephant", "mouse"]
    computerAnimal = random.choice(computerAnimalChoices)
    return computerAnimal


# Check wether or not the player or the computer won.
# Also keep track of there scores
def mainGame(playerAnimal, computerAnimal, playerScore, computerScore):
    if playerAnimal == computerAnimal:
        print("Argh, there was no battle you both chose",
              "{} it was a draw.".format(playerAnimal))
    elif playerAnimal == "lion":
        if computerAnimal == "mouse":
            print("Argh, you won lion beats mouse!",
                  "you are the king this time!")
            playerScore += 1
        else:
            print("Argh, you lost this one elephant beats lion!")
            computerScore += 1
    elif playerAnimal == "mouse":
        if computerAnimal == "elephant":
            print("Argh, you won this time mouse beats elephant,"
                  "this time your the king! but not for long!")
            playerScore += 1
        else:
            print("Argh, you lost this time lion beats up poor mouse!.")
            computerScore += 1
    elif playerAnimal == "elephant":
        if computerAnimal == "lion":
            print("Argh, you win this one elephant beats lion",
                  "you are the king! but not for long")
            playerScore += 1
        else:
            print("You loose computer chose mouse and mouse beats elephant")
            computerScore += 1

    # Let the user go back to the main menu
    input("Argh press enter to enter the main menu")
    utils.screenClear()
    playerAnimal, computerAnimal = "", ""
    return playerAnimal, computerAnimal, playerScore, computerScore


# This is the scoreboard that tells the players if they won or lost.
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


# Displays the messages you first see when you start the program.
utils.welcomeMessage()
utils.rulesScreen()

# Loop so they player can play again if they want to.
# This runs the game infintly unless the user stops it.
while True:
    # Runs the main menu
    playerAnimal, computerAnimal = menu(playerScore, computerScore)
    # Runs the main game and keeps track of scores.
    playerAnimal, computerAnimal, playerScore, computerScore = mainGame(playerAnimal, computerAnimal, playerScore, computerScore)
