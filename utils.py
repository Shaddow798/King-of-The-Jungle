import sys
import os
import pyfiglet
import time

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
    6. Pressing 0 will display the score and exit.""")
    input("Press the enter key to continue to the menu: ")
    screenClear()

# Display Welcome Message
def welcomeMessage():
    print(pyfiglet.figlet_format("Welcome to King of the Jungle."))
    time.sleep(3)
    screenClear()
