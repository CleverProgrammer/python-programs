from random import randint 

correct = 0

for i in range(10):
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    prod = n1 * n2
    
    ans = input("What's %d times %d? " % (n1, n2))
    if ans == prod:
        print "That's right -- well done.\n"
        correct = correct + 1
    else:
        print "No, I'm afraid the answer is %d.\n" % prod

print "\nI asked you 10 questions.  You got %d of them right." % correct
print "Well done!"
