from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

total = 0

def findFirst(a):
    for c in a:
        if c.isdigit():
            return int(c)

for d in dat:
    if d:
        total += findFirst(d)*10 + findFirst(d[::-1])

print(total)

