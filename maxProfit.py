class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) == 0:
            return 0
        min = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] - min > profit:
                profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]
        return profit