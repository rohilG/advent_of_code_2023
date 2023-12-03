from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
i,j = 0,0

total = 0

def getNum(i,j):
    num = []

    while j < len(dat[0]) and dat[i][j].isdigit():
        num.append(dat[i][j])
        j += 1

    return "".join(num)

def getRowGearRatio(i,j):
    initJ = j

    if j-1 >= 0 and dat[i][j-1].isdigit():
        while j-1 >= 0 and dat[i][j-1].isdigit():
            j -= 1

        num = getNum(i,j)
        
        if j + len(num) > initJ:
            return (1,int(num))

        # otherwise there's a POTENTIAL second num starting from initJ + 1
        if initJ+1 < len(dat[0]) and dat[i][initJ+1].isdigit():
            return (2,int(num)*int(getNum(i,initJ+1)))

        return (True,int(num))

    if dat[i][j].isdigit():
        return (1,int(getNum(i,j)))

    if j+1 < len(dat[0]) and dat[i][j+1].isdigit():
        return (1, int(getNum(i,j+1)))

    return (0, 1)


def getGearRatio(i,j):
    gearRatio = 1
    totalNumSeenNums = 0

    if i-1 >= 0: 
        numSeenNums, multipliedNums = getRowGearRatio(i-1,j)
        totalNumSeenNums += numSeenNums
        gearRatio *= multipliedNums

    # same row to gear's left
    if j-1 >= 0 and dat[i][j-1].isdigit():
        totalNumSeenNums += 1
        if (totalNumSeenNums > 2):
            return (False, gearRatio)

        rowInd = j-1
        num = []
        while rowInd >= 0 and dat[i][rowInd].isdigit():
            num.append(dat[i][rowInd])
            rowInd -= 1

        gearRatio *= int("".join(num[::-1]))

    # same row to gear's right
    if j+1 < len(dat[0]) and dat[i][j+1].isdigit():
        totalNumSeenNums += 1
        if totalNumSeenNums > 2:
            return (False, gearRatio)

        gearRatio *= int(getNum(i,j+1))

    if i+1 < len(dat):
        numSeenNums, multipliedNums = getRowGearRatio(i+1,j)
        totalNumSeenNums += numSeenNums
        if totalNumSeenNums > 2:
            return (False, 0)
        gearRatio *= multipliedNums

    if totalNumSeenNums == 2:
        return (True, gearRatio)
    return (False, 0)

while i < len(dat):
    j = 0
    while j < len(dat[0]):
        if dat[i][j] == "*":
            isGear, multipliedNums = getGearRatio(i,j)
            if isGear:
                total += multipliedNums
            
        j += 1
    i += 1

print(total)

