def minSizeSubSum(nums, target):
    r = l = total= 0
    minLen = float('inf')
    while r < len(nums):
        total += nums[r]
        while total >= target:
            minLen = min(minLen, r -l +1)
            total -= nums[l]
            l += 1
        r += 1
    return 0 if minLen == float('inf') else minLen
target = 7
nums = [2,3,1,2,4,3]
print(minSizeSubSum(nums, target))

