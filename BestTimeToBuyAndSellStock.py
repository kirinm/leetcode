class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        myMin = math.inf 
        for i in prices:
            myMin = min(myMin,i) 
            maxProfit = max(maxProfit,i-myMin)
        return maxProfit 