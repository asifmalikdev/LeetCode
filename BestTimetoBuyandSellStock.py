class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            if profit < price - min_price:
                profit = price - min_price

        return profit



obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))

print(obj.maxProfit([7,6,4,3,1]))
