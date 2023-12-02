from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

total = 0

def getPower(reaches):
    colorMap = {"red": 0, "green": 0, "blue":0}

    for reach in reaches:
        numColor = reach.split(", ")
        
        for nc in numColor:
            num,color = nc.split(" ")
            num = int(num)

            colorMap[color] = max(colorMap[color], num)
            
    return colorMap["red"]*colorMap["green"]*colorMap["blue"] 

for d in dat:
    game, acc = d.split(": ")
    reaches = acc.split("; ")
    total += getPower(reaches)

print(total)

