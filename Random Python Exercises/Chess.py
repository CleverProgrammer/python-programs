def main():
    for i in range(0,12):
        numberOfKids = eval(input("Enter Number of Kids Here: "))
        month = eval(input("Enter The Month: "))
        if month == 1:
            classesPerWeek = 5
        if month == 2:
            classesPerWeek = 5
        if month == 3:
            classesPerWeek = 5
        if month == 4:
            classesPerWeek = 5
        if month == 5:
            classesPerWeek = 5
        if month == 6:
            classesPerWeek = 0
        if month == 7:
            classesPerWeek = 3
        if month == 8:
            classesPerWeek = 0
        if month == 9:
            classesPerWeek = 5
        if month == 10:
            classesPerWeek = 5
        if month == 11:
            classesPerWeek = 5
        if month == 12:
            classesPerWeek = 5
        
        kids = numberOfKids*10*classesPerWeek
        money = kids * 6
        print (money)

main()


