def lengthOfLongestSubstring(s):
    maxLen = l = r =0
    d = {}
    while r < len(s):
        if s[r] in d and d[s[r]] >= l:
            l = d[s[r]] + 1
        maxLen = max(maxLen, r-l+1)
        d[s[r]] = r
        r += 1
    return d
# s = 'abcdecfab'
s = "abcabcbb"
print(lengthOfLongestSubstring(s))