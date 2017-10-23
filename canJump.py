class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here

        p = 0
        ans = 0
        for item in A[:-1]:
            ans = max(ans, p + item)
            if (ans <= p):
                return False
            p += 1
        return True

    def jump(self, A):
        # write your code here
        p = [0]
        for i in range(len(A) - 1):
            while (i + A[i] >= len(p) and len(p) < len(A)):
                p.append(p[i] + 1)
        return p[-1]


s = Solution()
print(s.jump([2,3,1,1,4]))