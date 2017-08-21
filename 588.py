import numpy as np
def canPartition(nums):
    sum = np.sum(nums)
    if sum & 1 != 0:
        return False
    else:
        sum = sum / 2
        dp = np.zeros((len(nums)+1,int(sum)+1))
        for i in range(len(nums)):
            for j in range(int(sum)):
                if j >= nums[i-1]:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-nums[i-1]]+nums[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
    return dp[len(nums)][sum] == sum