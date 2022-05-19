def characterReplacement(s,k):
    d = {}
    maxLen = l = 0
    for r in range(len(s)):
        d[s[r]] = 1 + d.get(s[r],0)
        while (r - l + 1) - max(d.values()) > k:
            d[s[r]] -= 1
            l += 1
        maxLen = max(maxLen,r - l +1)
    return maxLen

s = "AABABBA"
k = 2
print(characterReplacement(s,k))
