class Solution(object):
    # ===================================================================
    #  Dynamic Programming (DP) with 'memo' from bottom-up              =
    # ===================================================================
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ##  initialize dp table (need to include '0' element)
        dp_table = [0] + [float( 'inf' )] * amount

        for i in range( len( dp_table ) ) :
            for coin in coins :
                ##  no solution, skip
                if i - coin < 0 : continue

                dp_table[i] = min( dp_table[i], 1 + dp_table[i - coin] )

        return dp_table[i] if dp_table[i] != float( 'inf' ) else -1


    # ===================================================================
    #  Dynamic Programming (DP) with 'memo' from top-down               =
    # ===================================================================
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp_table = {}

        def dp( amount ):
            if amount in dp_table : return dp_table[amount]

            ##  base case handling
            if amount == 0 : return 0
            if amount  < 0 : return -1

            ##  initialize answer to infinity to find the minimum
            res = float( 'INF' )

            for coin in coins:
                ##  decrease the amount
                subproblem = dp( amount - coin )

                ##  no solution to subproblem, skip
                if subproblem == -1 : continue

                ##  find the min between previously / currently used number of coins (+1 for current loop)
                res = min( res, 1 + subproblem )

            dp_table[amount] = res if res != float( 'INF' ) else -1
            return dp_table[amount]

        return dp( amount )
