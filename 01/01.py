import functools

# Fuel required for each mass is the quotient of mass divided by 3 and then subtracted by 2
# Calculates total fuel required


def calculate_fuel(mass):
    fuel_needed = mass // 3 - 2
    if (fuel_needed <= 0):
        return 0
    return fuel_needed + calculate_fuel(fuel_needed)


f = open("input.txt", "r")
if f.mode == 'r':
    fuelList = [calculate_fuel(int(mass))
                for mass in f.read().splitlines()]
    totalFuelRequired = functools.reduce(lambda a, b: a + b, fuelList)
    print(totalFuelRequired)
    f.close()
