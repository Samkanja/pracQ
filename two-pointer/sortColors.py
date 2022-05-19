def sortColor(nums):
    r ,w = 0,0
    b = len(nums) - 1
    while w <= b:
        if  nums[w] == 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
            r += 1
        elif nums[w] == 1:
            w += 1
        else:
            nums[w], nums[b] = nums[b],nums[w]
            b -= 1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()        
nums = [2,0,1,1,2,0]
sortColor(nums)
print(printList(nums))