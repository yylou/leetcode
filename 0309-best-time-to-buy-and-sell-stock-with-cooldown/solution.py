class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  (base case)
        if len(prices) == 1: return 0
        
        # ==================================================
        #  Array + Dynamic Programming              (FSM)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        hold, noHold = float('-inf'), 0
        
        #  after selling stock, you cannot buy stock on the next day = NO HOLD state
        preDaySell = 0
        
        for price in prices:
            preHold, preNoHold = hold, noHold
            
            #  due to cooldown, cannot use preNoHold's profit to buy stock, use preDaySell
            hold   = max(preHold,   preDaySell - price)
            noHold = max(preNoHold, preHold    + price)
            
            #  record at the end to have an one-day gap (still 0 after 1st iteration)
            preDaySell = preNoHold
            
        return noHold