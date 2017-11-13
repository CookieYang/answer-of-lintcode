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


    def maxProfitIII(self,prices):
        l = len(prices)
        if l <= 0:
            return 0

        max , min= prices[l - 1], prices[0]
        left, right = [], []
        for i in range(1,l):
            if prices[i] >= min:
                if left[i-1] - min > prices[i] - min:
                    left[i] = left[i-1]
                else:
                    left[i] = prices[i] - min
            else:
                left[i] = left[i-1]
                min = prices[i]

        for j in range(l - 2, -1, 0):
            if prices[j] <= max:
                if right[j+1] > max - prices[j]:
                    right[j] = right[j+1]
                else:
                    right[j] = max - prices[j]
            else:
                right[j] = right[j+1]
                max = prices[j]

        max = -100;
        for i in range(0, l):
            if max > left[i] + right[i]:
                max = max
            else:
                max = left[i] +right[i]
        return max

