class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[left] > prices[right]:
                left = right
            right += 1
 
                
        return max_profit
