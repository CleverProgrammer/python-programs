def main():

    import random
    rn = random.randint(0,30)
    x = -1
    tally=0
    while x != rn:
        x = input("Enter Guess Number Here: ")
        if x == rn:
            print "You found the crack!"
        if x < rn:
            print "didn't crack!!"
        if x > rn:
            print "cracked!"
        tally=tally+1
    print "Tally = " + str(tally)

main()
    
        
    

        
