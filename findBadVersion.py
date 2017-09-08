def isBadVersion(cls):
    return cls >= 10

def findFirstBadVersion(n):
    left = 1
    right = n
    while left <= right:
        mid = int((left + right) / 2)
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


print(findFirstBadVersion(10))
