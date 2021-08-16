class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #  (base case)
        if len(prices) == 0 or len(prices) == 1: return 0

        # ==================================================
        #  Array + Dynamic Programming              (FSM)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        hold, noHold = float('-inf'), 0
        
        for price in prices:
            preHold, preNoHold = hold, noHold
            
            hold   = max(preHold,   preNoHold - price)
            noHold = max(preNoHold, preHold   + price - fee)
            
        return noHold