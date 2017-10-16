def sortColors2(colors, k):
    i = 0
    n = len(colors)
    while i < n:
        if colors[i] > 0:
            if colors[colors[i] - 1] > 0:
                tmp = colors[i]
                colors[i] = colors[colors[i] - 1]
                colors[tmp - 1] = -1
                i = i - 1
            else:
                colors[colors[i] - 1] -= 1
                colors[i] = 0
        i = i + 1

    i = len(colors) - 1
    k = i
    while i >= 0:
        if colors[i] < 0:
            pos = k + colors[i]
            while k > pos:
                colors[k] = i + 1
                k -= 1
        i -= 1

class Solution:
    def sortColors(self, nums):
        i = 0
        j = len(nums) - 1
        k = 0
        while k <= j:
            if nums[k] == 2:
                nums[j], nums[k] = nums[k],nums[j]
                j -= 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[i],nums[k] = nums[k],nums[i]
                i += 1
                k += 1

s = Solution()
num = [2,0,0,1,2,0,2]
s.sortColors(num)
print(num)