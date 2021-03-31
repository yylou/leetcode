class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        #:  Solution (1) use hash table to record 'suffix' information
        ans = [0] * (num+1)
        for i in xrange( num+1 ): ans[i] = ans[i>>1] + (i&1)
        return ans


        # ============================================================================ #


        #:  Solution (2) observe the pattern and use python built-in array 'extend'
        ans = [0]
        while len( ans ) <= num:
            ans.extend( [i+1 for i in ans] )
        return ans[:num+1]


        # ============================================================================ #


        #:  Solution (3) bit manipulation (XOR)
        rec = {0: 0, 1: 1}
        ans = [0] * (num+1)

        prevPower2 = -1
        for i in xrange( num+1 ):
            if i in rec: ans[i] = rec[i]

            #:  check whether i is power of 2
            elif (i & (i-1) == 0) and i != 0:
                prevPower2 = i
                ans[i] = 1
                rec[i] = 1

            #:  use hash table and prev power 2 element to do XOR
            else:
                rec[i] = rec[i^prevPower2]+1
                ans[i] = rec[i]

        return ans
