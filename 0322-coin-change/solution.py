class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        ##  (edge case) amount == 0, only one coin
        if amount == 0: return 0
        if len(coins) == 1 :
            remain = amount % coins[0]
            if remain == 0: return amount // coins[0]
            else: return -1

        coins.sort( reverse=True )   ##  start from the LARGEST value of coin
        global minVal
        minVal = amount + 1          ##  MAX amount = amount + 1 (by using coin with 1 value)

        def recursive( coinIndex=0, curUse=0, curAmount=amount ):
            global minVal

            curCoin = coins[coinIndex]
            result = curAmount // curCoin
            remain = curAmount % curCoin

            ##  FIND the answer, calculate MIN value
            if remain == 0:
                minVal = min( minVal, curUse+result )
                return

            if coinIndex == len(coins) - 1: return    ##  LAST coin, return
            if curUse + result + 1 > minVal: return   ##  MORE than MIN value, return

            ##  iterate each possible combination
            for i in range( result, -1, -1 ):
                recursive( coinIndex+1, i+curUse, curAmount-i*coins[coinIndex] )

        recursive()
        return minVal if minVal != amount+1 else -1
