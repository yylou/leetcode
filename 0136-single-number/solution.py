class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##  Soluition (1) mathemetical solution: 2 * ( a+b+c ) - (a+a+b+b+c) = c
        ##  use set to remove duplicate elements and sum the set, then minus the sum of original list
        return 2 * sum( set( nums ) ) - sum( nums )

        # =============================================================================================== #

        ##  Solution (2) bit manipulation: 'a' xor 'b' xor 'a' = ( 'a' xor 'a' ) xor 'b' = 0 xor b = b
        unique_num = 0
        for num in nums : unique_num ^= num
        return unique_num
