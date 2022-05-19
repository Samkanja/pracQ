def findAnagram(s,p):
    if len(p) > len(s): return []
    pDict = {}
    sDict = {}
    for i in range(len(p)):
        pDict[p[i]] = 1 + pDict.get(p[i],0)
        sDict[s[i]] = 1 + sDict.get(s[i],0)
    res = [0] if pDict == sDict else []
    l = 0
    for r in range(len(p),len(s)):
        sDict[s[r]] = 1 + sDict.get(s[r],0)
        if sDict[s[l]] == 1:
            del sDict[s[l]]
        else:
            sDict[s[l]] -= 1
        l += 1
        if sDict == pDict:
            res.append(l)

    return res

s = "cbaebabacd"
p = "abc"
print(findAnagram(s,p))