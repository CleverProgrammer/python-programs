def hydraulic_lift():
    mass_of_car = float(input("Weight of Car: "))
    piston_diamter = float(input("Diameter in m of car: "))
    car_diamter = float(input("Car rest diameter in m: "))
    height = float(input("Height of car: "))
    import math
    a1 = math.pi*((piston_diamter)/2.0)**2
    a2 = math.pi*((car_diamter)/2.0)**2
    m = mass_of_car
    g = 9.8
    f2 = m*g
    p = 900.0
    h = height
    f1 = (a1/a2)*f2+p*g*h*a1
    pressure = f1/a1
    print "Pressure: ", pressure
    print "Scientific Notation of Pressure: ", "%.3g" % pressure 
    return "Pressure: ", pressure

hydraulic_lift()
    
    
