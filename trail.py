def product(nums,k):
    count= l = 0
    total = 1
    for i in range(len(nums)):
        total *=nums[i]
        if total >= k:
            total /= nums[l]
            l += 1
        else:
            count +=1
    return count

nums=[10,5,2,6]
k = 100
print(product(nums,k))