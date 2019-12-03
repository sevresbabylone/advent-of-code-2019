def processInstructions(intCodeList):
    # last multiple of 4 accesses out-of-range indexes
    multiplesOfFour = range(0, len(intCodeList) - 4, 4)
    for i in multiplesOfFour:
        opCode = intCodeList[i]
        first_operand = intCodeList[intCodeList[i+1]]
        second_operand = intCodeList[intCodeList[i+2]]
        result_index = intCodeList[i+3]
        if(opCode == 99):
            break
        elif(opCode == 1):
            intCodeList[result_index] = first_operand + second_operand
        else:
            intCodeList[result_index] = first_operand * second_operand


def testVerbNoun(noun, verb, intCodeList, value):
    intCodeList[1] = noun
    intCodeList[2] = verb
    processInstructions(intCodeList)
    if (intCodeList[0] == value):
        print((noun, verb))


f = open("input.txt", "r")
if f.mode == "r":
    intCodeList = [int(x) for x in f.read().split(",")]
    for noun in range(99):
        for verb in range(99):
            testVerbNoun(noun, verb, intCodeList.copy(), 19690720)
