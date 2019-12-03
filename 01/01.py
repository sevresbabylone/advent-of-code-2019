import functools


def calculate_fuel_required(mass):
    return mass // 3 - 2


f = open("input.txt", "r")
if f.mode == 'r':
    fuelList = [calculate_fuel_required(int(mass))
                for mass in f.read().splitlines()]
    total = functools.reduce(lambda a, b: a + b, fuelList)
    print(total)
    f.close()
