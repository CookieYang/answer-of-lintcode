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