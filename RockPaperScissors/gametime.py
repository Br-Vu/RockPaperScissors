import random
import sys


def choice():
    global p1,p2,p1choice

    while True:
        p1choice = str.lower(input("R, P, or S? (Rock, Paper, Scissors?): "))
        if p1choice in ["r", "p", "s"]:
            break
        else:
            print("Incorrect choice, must be (r,p,s) try again.")
            continue

    if p1choice == "r":
        p1 = 1
        p1choice = "Rock"
    elif p1choice == "p":
        p1 = 2
        p1choice = "Paper"
    else:
        p1 = 3
        p1choice = "Scissors"
    p2 = random.randint(1, 3)
    print("Your choice is: " + p1choice)
    if p2 == 1:
        p2choice = "Rock"
    elif p2 == 2:
        p2choice = "Paper"
    else:
        p2choice = "Scissors"
    print("Opponent Choice is: " + p2choice)


def game_play():
    if p1 == p2:
        print("Tie Game")
    elif (p2 == 2 and p1 == 1) or (p2 == 3 and p1 == 2) or (p2 == 1 and p1 == 3):
        print("Opponent wins")
    else:
        print("You win")


def play_again():

    while True:
        selection = str.lower(input("Play again? y/n :"))
        if selection == "n":
            print("Thanks for playing!")
            sys.exit()
        elif selection == "y":
            break
        else:
            print("Incorrect choice, must be y/n try again.")
            continue
