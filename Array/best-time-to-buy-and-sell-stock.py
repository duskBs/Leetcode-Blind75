# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1147880412/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = prices[0]
        for item in prices:
            if item - lowest > maxP:
                maxP = item - lowest
            if item < lowest:
                lowest = item
        return maxP
