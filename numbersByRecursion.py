class Solution:
    def numbersByRecursion(self,n):
        if n <= 0:
            return []
        nums = []
        self.dfs(nums, n, 0)
        return nums

    def dfs(self, nums, n, cur):
        if n == 0:
            if cur > 0:
                nums.append(cur)
            return
        for i in range(0, 10):
            self.dfs(nums, n - 1, cur * 10 + i)



s = Solution()
s.numbersByRecursion(10)
