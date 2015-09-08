import math
import simplegui
import random

#Intializing global variables
global secret_number, number_of_tries, num_range
secret_number, number_of_tries, num_range = 0,0,0

# START AND STOP THE GAME [HELPER]
def new_game():
    global secret_number, number_of_tries, num_range
    secret_number, number_of_tries = 0,0
    if num_range == 100:
        range100()
    elif num_range == 1000:
        range1000()
    else: range100()

# [EVENT HANDLER]
# button that changes the range to [0,100) and starts a new game     
def range100():
    global secret_number, number_of_tries, num_range
    if num_range != 0:
        print
    
    print "New Game. Range is from 0 to 100"
    print "---------------------------------"
    low = 0
    high = 100
    num_range = high
    difference = high - low
    # formula: 2 ** n >= high - low + 1 --> Binary search [halving]
    # Solve for n, you get n >= ln(1000)/ln(2)
    # Automatically figures out needed tries
    number_of_tries = int(round(math.log(difference)/math.log(2),0))
    secret_number = random.randrange(low,high)
    print "Number of remaining guesses:", number_of_tries  

# [EVENT HANDLER]
# button that changes the range to [0,1000) and starts a new game     
def range1000():
    #CANNOT ADD PRINT("")
    global secret_number, number_of_tries, num_range
    print
    print "New Game. Range is from 0 to 1000"
    print "---------------------------------"
    low = 0
    high = 1000
    num_range = high
    difference = high - low
    # formula: 2 ** n >= high - low + 1 --> Binary search [halving]
    # Solve for n, you get n >= ln(1000)/ln(2)
    # Automatically figures out needed tries
    number_of_tries = int(round(math.log(difference + 1)/math.log(2),0))
    secret_number = random.randrange(low,high)
    print "Number of remaining guesses:", number_of_tries

# MAIN GAME
# [EVENT HANDLER]
def input_guess(guess):
    print
    global secret_number, number_of_tries
    guess = int(guess)
    print "Guess Was", guess
    
    if (guess != secret_number) and (number_of_tries == 1):
        print "You ran out of guesses. The number was",secret_number
        new_game()
    
    #NEEDS to be an elif. Otherwise once you run out of tries
    #The code continues anyways and ends up going to the 
    #ELSE statement, subtracting one try and printing 
    #The newly reduced number of tries.
    elif guess == secret_number:
        number_of_tries -= 1 #Decrease lives per turn
        print "Number of remaining guesses:", number_of_tries
        print "Correct!"
        new_game()
    
    elif guess > secret_number:
        number_of_tries -= 1 #Decrease lives per turn
        print "Number of remaining guesses:", number_of_tries
        print "Lower!"
    
    else:
        number_of_tries -= 1 #Decrease lives per turn
        print "Number of remaining guesses:", number_of_tries
        print "Higher!"
            
# [CREATE FRAME]
frame = simplegui.create_frame("Guess The Number", 200, 200)

# [REGISTER EVENT HANDLERS FOR CONTROL ELEMENTS & START FRAME]
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
frame.start()

# [CALL NEW GAME]
new_game()
