def twoSum(nums,target):
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d[target-n],i]
        d[n] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))