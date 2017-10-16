class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        i = 0
        j = len(nums) - 1
        num = 0
        while i < j:
            while nums[i] < k and i < j:
                i += 1
            while nums[j] >= k and i < j:
                j -= 1
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
        for i in range(len(nums)):
            if nums[i] < k:
                num += 1
            else:
                break
        return num

s = Solution()
print(s.partitionArray([7,7,9,8,6,6,8,7,9,8,6,6],10))