from collections import defaultdict
from math import inf

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()
lowest = inf

nums = [int(x) for x in dat[0].split(": ")[1].split(" ")]
ss,sf,fw,wl,lt,th,hl = [],[],[],[],[],[],[] 

ind = 2
m = -1
while ind < len(dat):
    if not dat[ind]:
        ind += 1
        continue
    elif not dat[ind][0].isdigit():
        ind += 1
        m += 1

    tempNums = [int(x) for x in dat[ind].split(" ")]
    destStart, sourceStart, length = tempNums[0],tempNums[1],tempNums[2]

    if m == 0:
        ss.append([sourceStart, destStart, length])
    elif m == 1:
        sf.append([sourceStart, destStart, length])
    elif m == 2:
        fw.append([sourceStart, destStart, length])
    elif m == 3:
        wl.append([sourceStart, destStart, length])
    elif m == 4:
        lt.append([sourceStart, destStart, length])
    elif m == 5:
        th.append([sourceStart, destStart, length])
    elif m == 6:
        hl.append([sourceStart, destStart, length])

    ind += 1

ss.sort(key=lambda x: x[0])
sf.sort(key=lambda x: x[0])
fw.sort(key=lambda x: x[0])
wl.sort(key=lambda x: x[0])
lt.sort(key=lambda x: x[0])
th.sort(key=lambda x: x[0])
hl.sort(key=lambda x: x[0])

#print(ss)
#print(sf)
#print(fw)
#print(wl)
#print(lt)
#print(th)
#print(hl)

def getValidNum(arr, num):
    #print(arr, num)

    for a,b,c in arr:
        if num-a >= 0 and num-a < c:
            return b + (num-a)

    # if num not found, return arr
    return num

def getDestNum(num):
    #print(num)

    a = getValidNum(ss,num)
    #print(a)

    b = getValidNum(sf,a)
    #print(b)

    c = getValidNum(fw,b)
    #print(c)

    d = getValidNum(wl,c)
    #print(d)

    e = getValidNum(lt, d)
    #print(e)

    f = getValidNum(th, e)
    #print(f)

    g = getValidNum(hl, f)
    #print(g)

    return g

total = 0
for i in range(0, len(nums), 2):
    total += nums[i+1]
print(total)

'''
for num in range(nums[0], nums[0]+nums[1]):
    destNum = getDestNum(num)
    lowest = min(lowest, destNum)

for num in range(nums[2], nums[2] + nums[3]):
    destNum = getDestNum(num)
    lowest = min(lowest, destNum)
'''

print(lowest)
