class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #:  (edge case) n == 1
        n = len(prices)
        if n == 1: return 0


        #:  Solution (1) reduced DP: iterate while maintaining local-min
        localmin, maxProfit = float('inf'), -float('inf')
        for i in xrange( n ):
            if prices[i] < localmin: localmin = prices[i]
            tmpResult = prices[i] - localmin
            if tmpResult > maxProfit: maxProfit = tmpResult

        return maxProfit


        # =========================================================================== #


        #:  Solution (2) standard DP: record local-min and local-max to calculate profit
        #:  - time complexity: O(n)
        #:  - space complexity: O(n)

        #:  (a) local min from left
        minRecord = [''] * n
        for i in xrange( n ):
            if i == 0: minRecord[i] = prices[i]
            else:
                if prices[i] < minRecord[i-1]: minRecord[i] = prices[i]
                else: minRecord[i] = minRecord[i-1]

        #:  (b) local max from right
        maxRecord = [''] * n
        for i in xrange( n-1, -1, -1 ):
            if i == n-1: maxRecord[i] = prices[i]
            else:
                if prices[i] > maxRecord[i+1]: maxRecord[i] = prices[i]
                else: maxRecord[i] = maxRecord[i+1]

        #:  (c) find the max profit
        maxProfit = -float('inf')
        for i in xrange( n ):
            tmpResult = maxRecord[i] - minRecord[i]
            if tmpResult > maxProfit: maxProfit = tmpResult

        return maxProfit
