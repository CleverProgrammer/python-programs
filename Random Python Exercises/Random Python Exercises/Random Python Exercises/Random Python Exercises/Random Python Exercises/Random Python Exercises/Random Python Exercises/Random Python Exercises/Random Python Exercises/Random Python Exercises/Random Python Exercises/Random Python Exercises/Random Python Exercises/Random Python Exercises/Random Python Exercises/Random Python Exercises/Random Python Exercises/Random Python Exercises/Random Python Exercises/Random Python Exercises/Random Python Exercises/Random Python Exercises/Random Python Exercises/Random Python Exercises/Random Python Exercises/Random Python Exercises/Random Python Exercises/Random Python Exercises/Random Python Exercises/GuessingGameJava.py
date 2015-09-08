#Design an alogrithm to play a number-guessing game
from random import randint
c = 1
d=1

while d != 0:
    randomNumber = randint(0,20) #randomly generated number
    while c != 0:
        
        guess = input("Enter your guess here:")
        if guess == randomNumber:
            print "You guessed correct\n"
            break
        elif guess < randomNumber:
            print "You are too low!"
        elif guess > randomNumber:
            print "You are too high!"
        
        
    
    d = raw_input("1 = again 0 = end\n")
