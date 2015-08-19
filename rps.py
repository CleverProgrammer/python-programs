print "Welcome to Rock, Paper, Scissors!"
from random import randint
continueRunning = 1
q = input("How many points would you like to play until? ")
c = 0 #Computer Score Tracker
h = 0 #Human Score Tracker
t = 0 #Tie Tracker
z = q #Same as q, how many points would you like to play until so no reason to re-enter value for z
#while continueRunning != 0:
while q > 0 and z > 0:
	print "\n"
	x = raw_input("(r)ock, (p)aper, (s)cissors? ")
	s = randint(1,3) #s = random number picked by the computer 
	if s == 1:
		print "Computer: Rock"
	if s == 2:
		print "Computer: Paper"
	if s == 3:
		print "Computer: Scissors"
	if x == 'r' or x == "rock":
		print "Human: Rock"
	if x == 'p' or x == "paper":
		print "Human: Paper"
	if x == 's' or x == "scissors":
		print "Human: Scissors"
	if s == 1 and (x == 's' or x == 'scissors'):
		c += 1
		z-=1
		print "|Computer Wins: " + str(c) + "|\n"
	if s == 2 and (x == 'r' or x == 'rock'):
		c += 1
		z-=1
		print "|Computer Wins: " + str(c) + "|\n"
	if s == 3 and (x == 'p' or x == 'paper'):
		c += 1
		z-=1
		print "|Computer Wins: " + str(c) + "|\n"
	if s == 1 and (x == 'p' or x == 'paper'):
		h += 1
		q -= 1
		print "|Human Wins: " + str(h) + "|\n"
	if s == 2 and (x == 's' or x == 'scissors'):
		h += 1
		q -= 1
		print "|Human Wins: " + str(h) + "|\n"
	if s == 3 and (x == 'r' or x == 'rock'):
		h += 1
		q -= 1
		print "|Human Wins: " + str(h) + "|\n"
	if s == 1 and (x == 'r' or x == 'rock'):
		t += 1
		print "|TIES: " + str(t) + "|"
	if s == 2 and (x == 'p' or x == 'paper'):
		t += 1
		print "|TIES: " + str(t) + "|"
	if s == 3 and (x == 's' or x == 'scissors'):
		t += 1
		print "|TIES: " + str(t) + "|"
	
			

	#continueRunning = input("1 = run again \n0 = end \n")
	if x == "end":
		break
print "Final Score: |Computer Wins: " + str(c) + "| " + "|Human Wins: " + str(h) + "| " + "|TIES: " + str(t) + "|"
