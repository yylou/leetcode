class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ##  (edge case)
        if n == 1 or n == 2: return n

        first, second = 1, 2
        for i in xrange( 3, n+1 ):
            first, second = second, first + second
        return second
