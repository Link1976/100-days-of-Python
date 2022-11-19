#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from random import *

logo = """  _______  __    __   _______     _______.     _______.   .___________.__    __   _______    .__   __.  __    __  .___  ___. .______    _______ .______      
 /  _____||  |  |  | |   ____|   /       |    /       |   |           |  |  |  | |   ____|   |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \     
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`   `---|  |----|  |__|  | |  |__      |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |    
|  | |_ | |  |  |  | |   __|     \   \        \   \           |  |    |   __   | |   __|     |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /     
|  |__| | |  `--'  | |  |____.----)   |   .----)   |          |  |    |  |  |  | |  |____    |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.
 \______|  \______/  |_______|_______/    |_______/           |__|    |__|  |__| |_______|   |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|
                                                                                                                                                              """

print(logo)

guess = randint(1, 100)   
attemps = 0
keep_playing = True

ask_level = True 
while ask_level:
    level = input("Select level: easy or hard:\n")
    if level == "easy": 
        print("You have 10 attempts. ")
        ask_level = False
    elif level == "hard":
        print("You have 5 attempts. ")
        ask_level = False
    else: 
        print("Select a correct level (easy or hard)")

def guess_number(number1, number2):
    if number1 < number2:
        print("the number is too low. ")
        keep_playing = True
        return keep_playing
    elif number1 > number2: 
        print("the number is too high")
        keep_playing = True
        return keep_playing
    else: 
        print("you guessed the number!!!")
        keep_playing = False
        return keep_playing

while keep_playing: 
    number = int(input("Guess the number between 1 to 100: \n"))
    keep_playing = guess_number(number, guess)
    print("You have wasted " + str(attemps+1) + " attemps. ")
    attemps += 1
    if level == "easy":
        if attemps == 10:
            print("You don't have more attempts")
            keep_playing = False
    elif level == "hard": 
        if attemps == 5:
            print("You don't have more attempts, the number was: " + str(guess))
            keep_playing = False

            




    

