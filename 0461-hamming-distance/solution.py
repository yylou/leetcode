##  Example
#       Input: x = 1, y = 4
#       Output: 2
#
#       Explanation:
#       1   (0 0 0 1)
#       4   (0 1 0 0)
#              ↑   ↑

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        ##  (1) using & to check the equlity of each bit
        ##  (2) using >> 1 for dividing number by 2, until both numbers become 0
        difference = 0

        while x>0 or y>0:
            if x&1 != y&1: difference +=1
            x, y = x>>1, y>>1

        return difference

        # ============================================================ #

        ##  (1) do XOR between two integers and convert to binary
        ##  (2) count the existence of bit 1 for the difference
        return bin( x ^ y )[2:].count( '1' )
