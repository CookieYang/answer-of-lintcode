def partition(array, left, right):
    if left > right : return -1
    pos = right
    right -= 1
    while left <= right:
        while left < pos and array[left] <= array[pos]: left += 1
        while right > left and array[right] > array[pos]: right -= 1
        if left >= right : break
        array[left], array[right] = array[right], array[left]
    array[left],array[pos] = array[pos],array[left]
    return left

def median(nums):
    if len(nums) == 0: return 0
    left = 0
    right = len(nums) - 1
    midIndex = right >> 1
    index = -1
    while index != midIndex:
        index = partition(nums, left ,right)
        if index < midIndex: left = index + 1
        elif index > midIndex: right = index + 1
        else: break
    return nums[index]