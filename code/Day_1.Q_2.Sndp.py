class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if prices:
            min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            compare_profit = price - min_price
            profit = max(compare_profit, profit)
        return profit