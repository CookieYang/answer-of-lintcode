class Solution:
    def numbersByRecursion(self,n):
        max = 10
        for i in range(1,n):
            max = max * 10
        max = max - 1
        return self.recursion(n, 0, 1, max)

    def recursion(self, n , depth, i, max):
        if depth >= n or i > max:
            return i;
        else:
            r = self.recursion(n, depth + 1, i+1, max)
            if r < max:
                self.recursion(n, 0, i+1, max)
            else:
                return r

s = Solution()
print(s.numbersByRecursion(3))
