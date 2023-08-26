# Leetcode question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
Solution:
Technique: Sliding Window
Complexity: O(n)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        i, j = 0, 1
        while (j <len(prices)):
            if prices[j] < prices[i]:
                i = j
            elif prices[j] > prices[i]:
                maxi = max(maxi, prices[j] - prices[i])
            j+=1
        return maxi       
