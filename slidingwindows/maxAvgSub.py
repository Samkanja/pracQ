def maxAvgSub(arr,k):
    maxSum = total = sum(arr[:k])
    x=0
    # i = k
    for i in range(k,len(arr)):
    # while i < len(arr):
        total += arr[i] - arr[x]
        maxSum = max(maxSum, total)
        x+=1
    return maxSum/k

nums = [1,12,-5,-6,50,3]
k = 4
print(maxAvgSub(nums,k))
