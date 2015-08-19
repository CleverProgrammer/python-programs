def study_session():
    for i in range (7):
        x = input("Input the number of pages: ")
        hoursToReadPage = (1.0/6.0)*x
        session = hoursToReadPage/2
        print (session)

study_session()
