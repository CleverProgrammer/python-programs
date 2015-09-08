bodyW = input("Enter your body weight in lbs:")
wristM = input("Enter your wrist measurement in inches:")
waistM = input("Enter your waist measurement in inches:")
hipM = input("Enter your hip measurement in inches:")
forearmM = input("Enter your forearm measurement in inches:")
a1 = (bodyW* 0.732) + (8.987)
a2 = (wristM) / (3.14)
a3 = (waistM) * (0.157)
a4 = (hipM) * (0.249)
a5 = (forearmM) * (0.434)
b = a1+a2-a3-a4+a5
bodyFat = bodyW - b
bodyFatPercentage = (bodyFat) * (100) / (bodyW)
print bodyFatPercentage
