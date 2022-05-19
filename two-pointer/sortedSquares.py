def sortedSquares(nums):
    res = []
    l , r = 0, len(nums) - 1
    while l <= r:
        if nums[l] * nums[l] > nums[r]*nums[r]:
            res.append(nums[l]*nums[l])
            l += 1
        else:
            res.append(nums[r]*nums[r])
            r -=1
    return res

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))

