from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

colorMap = {"red": 12, "green": 13, "blue":14}
colorMapSum = sum(map(int, colorMap.values()))
total = 0

def isValidGame(reaches):
    for reach in reaches:
        numColor = reach.split(", ")
        totalMarbles = 0
        
        for nc in numColor:
            num,color = nc.split(" ")
            num = int(num)

            if num > colorMap[color]:
                return False
            
            totalMarbles += num
            if totalMarbles > colorMapSum:
                return False

    return True

for d in dat:
    game, acc = d.split(": ")
    reaches = acc.split("; ")
    if isValidGame(reaches):
        total += int(game.split(" ")[1])

print(total)

