class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # (base case)
        if len(prices) == 0 or len(prices) == 1: return 0

        # ==================================================
        #  Array + Dynamic Programming              (FSM)  =
        # ==================================================
        # time  : O(n*k)
        # space : O(k)
        
        # '+1' for day 0 initialization
        T = k + 1
        hold, noHold = [float('-inf')] * T, [0] * T
        
        for price in prices:
            for i in range(1, T):
                prevHold, prevNoHold = hold[i], noHold[i]
                
                hold[i]   = max(prevHold,   noHold[i-1] - price)
                noHold[i] = max(prevNoHold, prevHold    + price)
                
        return noHold[-1]