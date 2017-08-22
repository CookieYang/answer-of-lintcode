def search(A, target):
    left = 0
    right = len(A)-1
    while left <= right:
        mid = int((left+right)/2)
        if A[mid] == target:
            return True
        if A[mid] > A[left]:
            if A[mid] > target and target > A[left]:
                right = mid
            else:
                left = mid + 1
        elif A[left] > A[mid]:
            if A[mid] < target and target <= A[right]:
                left = mid + 1
            else:
                right = mid
        else:
            left += 1
    return False
a = [3,4,4,5,7,0,1,2]
print(search(a,4))