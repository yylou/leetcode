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

            hold = max(preHold, 0 - price)
            sell = max(preSell, preHold + price)

        return sell

        '''

        """
        # ==================================================
        #  [Array] DP                          (localMin)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """

        # (base case)
        if len(prices) == 1: return 0

        localMin, maxProfit = float('inf'), float('-inf')
        for i in range(len(prices)):
            if prices[i] < localMin: localMin = prices[i]

            tmpProfit = prices[i] - localMin
            if tmpProfit > maxProfit: maxProfit = tmpProfit

        return maxProfit


        """
        # ==================================================
        #  [Array] DP                          (localMax)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """

        # (base case)
        if len(prices) == 1: return 0

        localMax, maxProfit = float('-inf'), float('-inf')
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > localMax: localMax = prices[i]

            tmpProfit = localMax - prices[i]
            if tmpProfit > maxProfit: maxProfit = tmpProfit

        return maxProfit

        '''
