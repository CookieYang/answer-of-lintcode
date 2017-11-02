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

print(cutting([1, 5, 8, 9, 10, 17, 17, 20],8))