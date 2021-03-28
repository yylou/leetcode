class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        #: Solution (1) shift n while '&' on current digit
        ans = 0
        while n:
            if n & 1: ans += 1
            n = n >> 1
        return ans


        # ========================================================================= #


        #: Solution (2) bit manipulation - 'least-significant 11-bit'
        ans = 0
        while n:
            ans += 1
            n &= n-1
        return ans


        # ========================================================================= #


        #: Solution (3) one-liner using python built-in function 'bin' and 'count'
        return str( bin(n) ).count( '1' )
