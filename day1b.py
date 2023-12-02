from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

total = 0
nums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}

# is short in beginning of long
def isInBeginning(long, short):
    if len(short) > len(long):
        return False

    for a,b in zip(short,long):
        if a != b:
            return False

    return True

def findFirst(a, isFlipped):
    for i,c in enumerate(a):
        if c.isdigit():
            return int(c)

        for num in nums:
            if isFlipped:
                if isInBeginning(a[i:], num[::-1]):
                    return nums[num]
            elif isInBeginning(a[i:], num):
                return nums[num] 

    return 0

for d in dat:
    if d:
        total += findFirst(d,False)*10 + findFirst(d[::-1], True)

print(total)

