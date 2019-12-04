import functools


def getLineCoordinates(currentCoordinate, directionString):
    directions = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0]
    }
    nextCoordinates = []
    currentDirection = directions.get(directionString[0])
    scalar = int(directionString[1:])
    x = currentCoordinate[0]
    y = currentCoordinate[1]
    while(scalar != 0):
        x = x + currentDirection[0]
        y = y + currentDirection[1]
        nextCoordinates.append((x, y))
        scalar = scalar - 1
    return nextCoordinates


def getPathCoordinates(path):
    allCoordinates = []
    currentCoordinate = (0, 0)
    for x in path.split(","):
        allCoordinates = allCoordinates + \
            getLineCoordinates(currentCoordinate, x)
        # removes (0,0)
        currentCoordinate = allCoordinates[-1]
    return allCoordinates


f = open("input.txt", "r")
if f.mode == "r":
    wires = [getPathCoordinates(path) for path in f.read().splitlines()]
    intersections = set(wires[0]) & set(wires[1])  # lulz
    manhattanDists = [abs(i[0]) + abs(i[1]) for i in intersections]
    print(functools.reduce(lambda a, b: a if a < b else b, manhattanDists))
    print(intersections)

    intersectionsDistances = [
        (wires[0].index(i) + wires[1].index(i) + 2) for i in intersections]
    print(min(intersectionsDistances))
