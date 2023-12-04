from collections import defaultdict

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
total = 0

for d in dat:
    numDouble = -1

    win,nums = d.split(": ")[1].split(" | ")
    win = win.split(" ")
    nums = nums.split(" ")

    #print(win,nums)

    for w in win:
        if w and w[0].isdigit() and w in nums:
            numDouble += 1
            #print(w)
   
    if numDouble != -1:
        total += 2**numDouble
        #print(2**numDouble)
    
    #print()

print(total)
