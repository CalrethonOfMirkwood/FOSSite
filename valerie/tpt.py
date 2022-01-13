import random

def guesser():
    guesses = 5
    randpaul = random.randint(0, 10)
    playagain = ""
    guess = int(input("guess a number 1-10 pls "))
    while guesses > 0:
        if guess == randpaul:
            playagain = str(input("contratulations! yuove won!! play again? 'yes' or 'no' "))
            while playagain != "yes" and playagain != "no":
                playagain = input("pls enter 'yes' or no' kthx (use quotation marks)")
                if playagain == "yes":
                    guesser()
                else:
                    exit()
        else:
            guesses -= 1
            guess = input("no thats wrong try again ")
            if guesses == 0:
                print("you lost sorry babe ")
                exit()
