class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        purchased = prices[0]
        for i in range(len(prices)):
            if (prices[i] > purchased):
                maxProfit += prices[i] - purchased
            purchased = prices[i]
        return maxProfit