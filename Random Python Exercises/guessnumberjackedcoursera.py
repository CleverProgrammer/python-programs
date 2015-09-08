import math
import simplegui
import random

#Intializing global variables
global secret_number, number_of_tries
secret_number, number_of_tries = 0,0

# helper function to start and restart the game
def new_game():
    print
    global secret_number, number_of_tries
    secret_number, number_of_tries = 0,0

# define event handlers for control panel
# button that changes the range to [0,100) and starts a new game     
def range100():
    new_game()
    print "New Game. Range is from 0 to 100"
    print "---------------------------------"
    global secret_number, number_of_tries
    low = 0
    high = 100
    difference = high - low
    # formula: 2 ** n >= high - low + 1 --> Binary search [halving]
    number_of_tries = int(round(math.log(difference + 1)/math.log(2),0))
    secret_number = random.randrange(low,high)
    print "Number of remaining guesses:", number_of_tries  

# button that changes the range to [0,1000) and starts a new game     
def range1000():
    new_game()
    print "New Game. Range is from 0 to 1000"
    print "---------------------------------"
    global secret_number, number_of_tries
    low = 0
    high = 1000
    difference = high - low
    # formula: 2 ** n >= high - low + 1 --> Binary search [halving]
    # Solve for n, you get n >= ln(1001)/ln(2)
    number_of_tries = int(round(math.log(difference + 1)/math.log(2),0))
    secret_number = random.randrange(low,high)
    print "Number of remaining guesses:", number_of_tries

def input_guess(guess):
    # main game logic goes here	
    print
    global secret_number, number_of_tries
    guess = int(guess)
    print "Guess Was", guess
    
    if (guess != secret_number) and (number_of_tries == 1):
        print "You ran out of guesses. The number was",secret_number
        print
        range100()
    
    #NEEDS to be an elif. Otherwise once you run out of tries
    #The code continues anyways and ends up going to the 
    #ELSE statement, subtracting one try and printing 
    #The newly reduced number of tries.
    elif guess == secret_number:
        guess = secret_number
        print "Correct!"
        print "Number of remaining guesses:", number_of_tries
        print
        range100()
    
    elif guess > secret_number:
        number_of_tries -= 1 #Decrease lives per turn
        print "Number of remaining guesses:", number_of_tries
        print "Lower!"
    
    else:
        number_of_tries -= 1 #Decrease lives per turn
        print "Number of remaining guesses:", number_of_tries
        print "Higher!"
            
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
frame.start()
range100()

# always remember to check your completed program against the grading rubric
