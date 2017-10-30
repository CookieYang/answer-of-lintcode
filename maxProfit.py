import  sys
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

    def maxProfitII(self,prices):
        total = 0
        low, high = sys.maxint, sys.maxint
        for x in prices:
            if x > high:
                high = x
            else:
                total += high - low
                high, low = x, x
        return total + high - low
