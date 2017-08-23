def binarySearch(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = int((left + right) / 2)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[right] == target:
        return right
    return -1

def searchInsert(A, target):
    left = 0
    right = len(A) - 1
    if right == -1:
        return 0
    while left < right:
        mid = int((left + right) / 2)
        if A[mid] > target:
            right = mid
        elif A[mid] < target:
            left = mid + 1
        else:
            return mid
    if  target > A[-1]:
        return len(A)
    return right

print(searchInsert([1,3,5,6],7))
