#Guessing game
#W4RM15H
#29/08/18

#IMPORTS
import random
from termcolor import colored as c
from os import system

#STORED VARIABLES
class vars():
    player_name = "Player 1"
    number_to_guess = 0
    guesses = 0

#PLAY AGAIN FUNCTION
def play_again():
    play_again = input("Congrats, wonna play again? y or n\n > ")
    if play_again == "yes" or "y":
        playing_game()
    else:
        print("Quitting...")
        exit()

#SHOWING GAME RESULT
def game_result(result):
    system('clear')
    print("{0}".format(result))

#INTRO TO GAME 
def game_intro():
  print("Guessing the number game!")
  print()
  vars.player_name = input("Enter your name \n > ")
  print()
  play_game = input(c('Press enter to play', 'green'))
  if play_game == "":
    playing_game()
  else:
    exit()

#ACTUAL GAME FUNCTION
def playing_game():
    system('clear')
    vars.number_to_guess = random.choice(range(1,10))
    while True:       
        print("Alright {0}!".format(vars.player_name))
        player_guess = int(input("Guess a number between 1 and 10\n > "))

        if player_guess == vars.number_to_guess:
            game_result("Good Work")
            print('It took you {0} guesses'.format(vars.guesses))
            play_again()    
               
        if player_guess <= vars.number_to_guess:
            print("Try a number a little higher")
            vars.guesses += 1

        if player_guess >= vars.number_to_guess:
            print("Try a lower number")
            vars.guesses += 1

        else:
            print("Please enter a valid input")
if __name__ == "__main__":
    game_intro()
