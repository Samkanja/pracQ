def totalFruits(fruits):
    d = {}
    r = l = maxLen = 0
    while r < len(fruits):
        d[fruits[r]] = r
        if len(d) >= 3:
            minVal = min(d.values())
            del d[fruits[minVal]]
            l = minVal + 1
        maxLen = max(maxLen, r -l +1)
        r += 1
    return maxLen
# fruits = [0,1,2,2]
fruits = [1,1,2,3,2,2]
print(totalFruits(fruits))  

