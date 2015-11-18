import random


def run():
    mylist = []
    for i in range(random.randint(1, 10)):
        random.seed(0)
        if random.randint(1, 10) > 0:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print mylist
run()
