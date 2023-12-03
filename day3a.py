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

def rowHasStar(numLen,i,j):
    for rowInd in range(j-1, j + numLen + 1):
        if rowInd >= 0 and rowInd < len(dat[0]):
            if dat[i][rowInd].isdigit() == False and dat[i][rowInd] != ".":
                return True

    return False

def isPartNumber(numLen,i,j):
    if i-1 >= 0 and rowHasStar(numLen,i-1,j):
        return True

    if rowHasStar(numLen,i,j):
        return True

    if i+1 < len(dat) and rowHasStar(numLen,i+1,j):
        return True

    return False

while i < len(dat):
    j = 0
    while j < len(dat[0]):
        if dat[i][j].isdigit():
            num = getNum(i,j)
            print(num)

            if isPartNumber(len(num), i,j):
                total += int(num)

            while j < len(dat[0]) and dat[i][j].isdigit():
                j += 1
            j -=1

        j += 1
    i += 1

print(total)

