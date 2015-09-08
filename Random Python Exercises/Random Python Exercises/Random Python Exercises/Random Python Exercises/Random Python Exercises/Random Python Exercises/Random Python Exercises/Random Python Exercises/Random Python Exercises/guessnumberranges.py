# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import simplegui
import random

#Intializing
global secret_number, number_of_tries
secret_number, number_of_tries = 0,0


# helper function to start and restart the game
def new_game():
    global secret_number, number_of_tries
    
    # initialize global variables used in your code here

    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    newgame()
    low = 0
    high = 100
    difference = high - low
    # formula: n ** 2 >= high - low + 1 --> Binary search [halving]
    number_of_tries = int(round(math.log(difference + 1)/math.log(2),0))
    global secret_number, number_of_tries
    secret_number = random.randint(0,100)
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    newgame()
    low = 0
    high = 1000
    difference = high - low
    # formula: n ** 2 >= high - low + 1 --> Binary search [halving]
    number_of_tries = int(round(math.log(difference + 1)/math.log(2),0))
    global secret_number, number_of_tries
    secret_number = random.randint(low,high)
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    if guess == secret_number:
        print "Correct"
    elif guess > secret_number:
        print "Lower"
    else:
        print "Higher"
    # remove this when you add your code
    pass

    
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("range100",range100,100)
frame.add_button("range1000",range1000,100)
frame.add_input("input guess", input_guess, 100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
