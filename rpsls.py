# Rock-paper-scissors-lizard-Spock

import random
import math

#Converts names to numbers for computer to evaluate
def name_to_number(name):
    if name == "rock":
        return 0
    if name == "Spock":
        return 1
    if name == "paper":
        return 2
    if name == "lizard":
        return 3
    if name == "scissors":
        return 4

#Converts numbers to names for humans to visualize
def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number == 4:
        return "scissors"
    
#Actual game logic    
def rpsls(player_choice): 
    print
    print "Player chooses " + str(player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + str(comp_choice)
    #difference variable for calculating result
    difference = (comp_number-player_number)%5
    if (difference == 1) or (difference == 2):
        print "Computer wins!"
    elif (difference == 3) or (difference == 4):
        print "Player wins!"
    else:
        print "Player and computer tie!"
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



