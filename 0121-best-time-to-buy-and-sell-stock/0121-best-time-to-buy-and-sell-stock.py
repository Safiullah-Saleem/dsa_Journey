from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy pointer
        right = 1  # Sell pointer
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:  
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right  # Move left to the current right index
                
            right += 1  # Always move right pointer forward

        return maxProfit
