class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        #max_sell = 0
        for i in range(1,len(prices)):
            min_buy = min(min_buy,prices[i])
            #max_sell = max(max_sell,prices[i])
            max_profit = max(max_profit,prices[i]-min_buy)
        return max_profit