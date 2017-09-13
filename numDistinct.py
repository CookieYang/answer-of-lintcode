def numDistinct(S, T):
    ls = len(S)
    lt = len(T)
    dp = [[0 for i in range(ls + 1)] for i in range(lt + 1)]
    dp[0][0] = 1
    for j in range(1,ls+1):
        dp[0][j] = 1
    for i in range(1,lt + 1):
        for j in range(1, ls + 1):
            dp[i][j] = dp[i][j - 1]
            if T[i - 1] == S[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return  dp[lt][ls]
c = numDistinct('rabbbit','rabbit')
print(c)