class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  (base case)
        if len(prices) == 0 or len(prices) == 1: return 0
        
        # ==================================================
        #  Array + Dynamic Programming              (FSM)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        # '+1' for day 0 initialization
        T = 2 + 1
        hold, noHold = [float('-inf')] * T, [0] * T
        
        for price in prices:
            for i in range(1, T):
                preHold, preNoHold = hold[i], noHold[i]
                
                hold[i]   = max(preHold,   noHold[i-1] - price)
                noHold[i] = max(preNoHold, preHold     + price)
                
        return noHold[-1]