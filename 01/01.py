def calculate_fuel_required(mass):
    return mass // 3 - 2


f = open("input.txt", "r")
if f.mode == 'r':
    fuelList = [calculate_fuel_required(int(mass))
                for mass in f.read().splitlines()]
    total = 0
    for fuel in fuelList:
        total += fuel
    print(total)
    f.close()
