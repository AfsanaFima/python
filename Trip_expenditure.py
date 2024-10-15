def h_cost(night):
    return 44*night

def p_r_cost(city) :
    if "city1" == city:
        return 554
    elif"city2" == city:
        return 536
    elif"city3" == city:
        return 53
    elif"city4" == city:
        return 365
    
def r_car_cost (days):
    if days >=7 :
        return 55*days - 50
    elif days >=3 :
        return 55*days - 30
    else:
        return 40*days
    
def trip_cost (city,days,s_m) :
    return r_car_cost(days) + h_cost(days) + p_r_cost(city) + s_m

print("Cost of rental car is : ",r_car_cost(8))
print("Cost of plane ride is : ",p_r_cost("city3"))
print("Cost of hotel rooma are : ",h_cost(7))
print("cost of the whole trip is : ",trip_cost("city3",7,5098))


