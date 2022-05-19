def lenOfRepchar(s,k):
    maxLen = r = l = 0
    d = {}
    while r < len(s):
        d[s[r]] = 1 + d.get(s[r],0)
        if (r - l + 1) - max(d.values()) > k:
            d[s[l]] -= 1
            l  += 1
        maxLen = max(maxLen,r -l +1)
        r += 1
    return maxLen


# s = "ABAB"
s = "AABABBA"
k = 2
# # k = 1
# s=[1,1,1,0,0,0,1,1,1,1,0]
# s= [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
print(lenOfRepchar(s,k))
