from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
total = 0
cardMap = defaultdict(int)

def getNumMatching(d):
    numMatch = 0

    win,nums = d.split(": ")[1].split(" | ")
    win = win.split(" ")
    nums = nums.split(" ")

    for w in win:
        if w and w[0].isdigit() and w in nums:
            numMatch += 1 
            #print(w)
   
    return numMatch

for d in dat:
    cardNum = int(d.split(": ")[0].split(" ")[-1])
    numMatching = getNumMatching(d)

    #print(cardNum,numMatching, end =" ")

    cardMap[cardNum] += 1

    for i in range(numMatching):
        cardMap[cardNum+1+i] += cardMap[cardNum] 

    #print(cardMap)


print(sum(map(int, cardMap.values())) )
