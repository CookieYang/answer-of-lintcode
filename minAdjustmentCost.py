import sys
def MinAdjustmentCost(A, target):
    # write your code here
    f = [[sys.maxint for j in range(101)] for i in range(len(A) + 1)]
    for i in range(101):
        f[0][i] = 0
    n = len(A)
    for i in range(1, n + 1):
        for j in range(101):
            if f[i - 1][j] != sys.maxint:
                for k in range(101):
                    if abs(j - k) <= target:
                        f[i][k] = min(f[i][k], f[i - 1][j] + abs(A[i - 1] - k))
    ans = f[n][100]
    for i in range(101):
        if f[n][i] < ans:
            ans = f[n][i]

    return ans

def cutting(prices, n):
    r = [0]
    for i in range(1, n + 1):
        p = -1000
        for j in range(1, i + 1):
            p = max(p, prices[j - 1] + r[i - j])
        r.append(p)
    return r[n]

def houseRobber(A):
    cur, last, be_last = 0, 0, 0
    for i in range(len(A)):
        cur = max(last, be_last + A[i])
        be_last = last
        last = cur
    return cur

def houseRobberII(A):
    return max(houseRobber(A[1:]),houseRobber(A[:-1]))

def houseRobber3(self, root):
        # write your code here
    rob, not_rob = self.visit(root)
    return max(rob, not_rob)

def visit(self, root):
    if root is None:
        return 0, 0

    left_rob, left_not_rob = self.visit(root.left)
    right_rob, right_not_rob = self.visit(root.right)

    rob = root.val + left_not_rob + right_not_rob
    not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
    return rob, not_rob

def numWays(n, k):
        # write your code here
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k
    pre, now = k, k * k
    for i in range(3, n + 1):
        tmp = now
        now = (pre + now) * (k - 1)
        pre = tmp
    return now

print(houseRobberII([3,6,4]))