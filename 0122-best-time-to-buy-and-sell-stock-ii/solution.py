class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        # ==================================================
        #  [Array] DP                                      =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """

        # (base case)
        if len(prices) == 1: return 0

        hold, sell = float('-inf'), 0

        for price in prices:
            preHold, preSell = hold, sell

            hold = max(preHold, preSell - price)
            sell = max(preSell, preHold + price)

        return sell
