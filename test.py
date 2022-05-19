def sortColor(nums):
    l ,i, r = 0, 0,len(nums) -1
    while i <= r:
        if nums[i] == 0:
            nums[i],nums[l] = nums[l],nums[i]
            l += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
            i -= 1
        i += 1
    return

nums = [2,0,1,1,2,0]
print(sortColor(nums)) 