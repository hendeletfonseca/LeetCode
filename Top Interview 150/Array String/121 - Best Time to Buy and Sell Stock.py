class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lastLess = prices[0]
        for i in range(len(prices)):
            current = prices[i]
            if (lastLess > current):
                lastLess = current
            profit = current - lastLess
            if (profit > maxProfit):
                maxProfit = profit
        return maxProfit