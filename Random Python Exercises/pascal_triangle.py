#Binomial experiment proving the theorem of the pascal triangle.
#Flip 16 sets of 4 reps each.
#General results of 16 sets of 4 reps should be ~ 1 4 6 4 1

#    Pascal's_Triangle           
#           /1\       #2^0 = 1  #1/1 chance of getting all heads out of 0 attempt
#          /1 1\      #2^1 = 2  #1/2 chance of getting all heads out of 1 attempts
#         /1 2 1\     #2^2 = 4  #1/4 chance of getting all heads out of 2 attempts
#        /1 3 3 1\    #2^3 = 8  #1/8 chance of getting all heads out of 3 attempts
#       /1 4 6 4 1\   #2^4 = 16 #1/16 chance of getting all heads out of 4 attempts
#     /1 5 10 10 5 1\ #2^5 = 32 #1/32 chance of getting all heads out of 5 attempts
#     ----------------      
#Encorporating Percentage Error as well
#Percentage Error = (Actual Score - Correct Score)/(Correct Score)
#Answer is more viable if percentage error result is near 0

def coin_flips(local_n):
    LTF = 0 #Local Tail-Flip
    LHF = 0 #Local Head-Flip
    import random
    while LTF + LHF < local_n:
        RN = random.randint(0,1) #Random Number Generator 0-1
        if RN == 0:
            LHF += 1
        else:
            LTF += 1
    return LHF,LTF

def head_counter(NF):
    count = 0
    head_c0 = 0
    head_c1 = 0
    head_c2 = 0
    head_c3 = 0
    head_c4 = 0
    while count < NF:
        n=4
        (HF,TF)=coin_flips(n)
        if HF == 4:
            head_c4 += 1
        if HF == 3:
            head_c3 += 1
        if HF == 2:
            head_c2 += 1
        if HF == 1:
            head_c1 += 1
        if HF == 0:
            head_c0 += 1
        count += 1
    print "test new formula: " + str(abs((head_c4/NF)-(1/16.0)))
    #p_e4 =abs((head_c4-(10000.0))/(10000.0)) # % Error. Close to 0 is good
    #p_e3 =abs((head_c3-(40000.0))/(40000.0)) # (c4/n)-(1/16)
    #p_e2 =abs((head_c2-(60000.0))/(60000.0))
    #p_e1 =abs((head_c1-(40000.0))/(40000.0))
    #p_e0 =abs((head_c0-(10000.0))/(10000.0))
    print "head_c4 (10000): " + str(head_c4)," head_c3(40000): " + str(head_c3)," head_c2(60000): " + str(head_c2)," head_c1(40000): " + str(head_c1)," head_c0(10000): " + str(head_c0)
    #print "\np_e4: " + str(p_e4)," p_e3: " + str(p_e3)," p_e2: " + str(p_e2)," p_e1: " + str(p_e1)," p_e0: " + str(p_e0)
NF = input("Enter Number of Flips: ")
head_counter(NF)
