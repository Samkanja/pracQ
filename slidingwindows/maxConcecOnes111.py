def longestOnes(nums, k):
    l = r = maxLen = flips =0
    while r < len(nums):
        flips += 1 - nums[r]
        if flips > k:
            flips -= 1 - nums[l]
            l += 1
        if flips <= k:
            maxLen = max(maxLen, r - l +1)
        r += 1

    return maxLen
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))

