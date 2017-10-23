class Solution:

    def dfs(self,n,k,m,p,tmp,res):
        if k == p:
            res.append(tmp[:])
            return
        for i in range(m, n + 1):
            tmp.append(i)
            self.dfs(n,k,i+1,p+1,tmp,res)
            tmp.pop()

    def combine(self, n, k):
        res = []
        tmp = []
        self.dfs(n,k,1,0,tmp,res)
        return res

s = Solution()
print(s.combine(4,2))