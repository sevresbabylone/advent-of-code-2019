import functools

# Fuel required for each star is the quotient of mass divided by 3 and then subtracted by 2
# Calculates total fuel required


def calculate_fuel_required(mass):
    return mass // 3 - 2


f = open("input.txt", "r")
if f.mode == 'r':
    fuelList = [calculate_fuel_required(int(mass))
                for mass in f.read().splitlines()]
    totalFuelRequired = functools.reduce(lambda a, b: a + b, fuelList)
    print(totalFuelRequired)
    f.close()
