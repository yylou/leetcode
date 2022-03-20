class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        """
        # ==================================================
        #  [Array] DP                                      =
        # ==================================================
        # time  : O(nk)
        # space : O(k)
        """

        # (base case)
        if len(prices) == 1: return 0

        T = k + 1
        hold, sell = [float('-inf')] * T, [0] * T

        for price in prices:
            for i in range(1, T):
                preHold, preSell = hold[i], sell[i]

                hold[i] = max(preHold, sell[i-1] - price)
                sell[i] = max(preSell, preHold + price)

        return max(sell)
