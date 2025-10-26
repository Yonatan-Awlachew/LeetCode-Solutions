class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        profit,min_price = 0,float("inf")
        for x in prices:
            if x<min_price: min_price = x
            else:
                profit = max(profit,x-min_price)
        return profit
