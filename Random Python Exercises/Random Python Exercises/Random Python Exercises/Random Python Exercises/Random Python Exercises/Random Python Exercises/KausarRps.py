print "Welcome to Rock, Paper, Scissors!"
from random import randint
continueRunning = 1
q = input("Enter Number of Scores to Win: ")
n = 0 #Computer Score Tracker
m = 0 #Waqas Score Tracker
t = 0 #Tie Tracker
z = q
#while continueRunning != 0:
while q > 0 and z > 0:
	print "\n"
	x = raw_input("(r)ock, (p)aper, (s)cissors? ")
	s = randint(1,3) #s = random number
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
		n += 1
		z-=1
		#print "Score: ", n
		print "|Computer Wins: " + str(n) + "|"
	if s == 2 and (x == 'r' or x == 'rock'):
		n += 1
		z-=1
		#print "Score: ", n
		print "|Computer Wins: " + str(n) + "|"
	if s == 3 and (x == 'p' or x == 'paper'):
		n += 1
		z-=1
		#print "Score: ", n
		print "|Computer Wins: " + str(n) + "|"
	if s == 1 and (x == 'p' or x == 'paper'):
		m += 1
		q -= 1
		#print "Score: ", m
		print "|Waqas Wins: " + str(m) + "|"
	if s == 2 and (x == 's' or x == 'scissors'):
		m += 1
		q -= 1
		#print "Score: ", m
		print "|Waqas Wins: " + str(m) + "|"
	if s == 3 and (x == 'r' or x == 'rock'):
		m += 1
		q -= 1
		#print "Score: ", m
		print "|Waqas Wins: " + str(m) + "|"
	if s == 1 and (x == 'r' or x == 'rock'):
		t += 1
		#print "Score: ", t
		print "|TIES: " + str(t) + "|"
	if s == 2 and (x == 'p' or x == 'paper'):
		t += 1
		#print "Score: ", t
		print "|TIES: " + str(t) + "|"
	if s == 3 and (x == 's' or x == 'scissors'):
		t += 1
		#print "Score: ", t
		print "|TIES: " + str(t) + "|"
	#if x == \e:
		#break
			

	#continueRunning = input("1 = run again \n0 = end \n")
	if x == "end":
		break
print "Final Score: |Computer Wins: " + str(n) + "| " + "|Waqas Wins: " + str(m) + "| " + "|TIES: " + str(t) + "|"
