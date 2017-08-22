def sqrt(x):
    low = 0
    high = int(x)
    while low <= high:
        mid = int((low + high) / 2)
        if mid * mid > x:
            high = mid - 1
        elif mid * mid < x:
            low = mid + 1
        else:
            return mid
    return high

print(sqrt(9))


