import numpy as np
import math
def nextPermutaion(nums):
    n = len(nums)
    if n == 1:
        return
    for i in range(1,n):
        if nums[n-i-1] < nums[n-i]:
            for j in range(1,i):
                if nums[n-j] > nums[n-i-1]:
                    nums[n-i-1],nums[n-j] = nums[n-j],nums[n-i-1]
                    pre = list(nums[0:n-i])
                    suf = list(nums[n-i:n])
                    suf.reverse()
                    nums = pre + suf
                    return nums

a = [1,3,2]
print(nextPermutaion(a))