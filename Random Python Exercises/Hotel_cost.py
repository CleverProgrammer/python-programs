def hotel_cost(nights):
    return 95.83*nights

def plane_ride_cost(city):
    if city == "Las Vegas":
        return 180*3

def rental_car_cost(days):
    everyday = 40*days
    if days >= 7:
        return (everyday) - 50
    elif days >= 3:
        return (everyday) - 20
    else:
        return everyday

def trip_cost(city, days, spending_money, tournament_fee):
    return  plane_ride_cost(city) + hotel_cost(days) + spending_money + tournament_fee

print trip_cost("Las Vegas", 6, 600, 1000)
print hotel_cost(6)
print plane_ride_cost("Las Vegas")
