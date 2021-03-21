class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ##  (edge case) 'nums' is empty / 'nums' only has one element
        if not nums: return []
        if len( nums ) == 1:
            if nums[0] != 1: return [1]
            else: return [2]


        ##  Solution (1) using 'set' to remove duplicate items
        ##  - time complexity: O(n)
        return set( range( 1, len(nums)+1 ) ) - set(nums)


        # ============================================================================= #


        ##  Solution (2) two-pass scan to MODIFY input list and RECORD missing elements
        ##  - time complexity: O(n)
        missingNum = []

        ##  1st Scan: Mark existing number by converting it to NEGATIVE value
        for i in xrange( len(nums) ):
            curVal = abs( nums[i] )

            if curVal == len(nums): nums[0] = False
            else: nums[curVal] = -1 * abs( nums[curVal] )

        ##  2nd Scan: RECORD the number with POSITIVE value as missing one
        for i in xrange( 1, len(nums) ):
            if nums[i] > 0: missingNum.append( i )

        if nums[0] > 0: missingNum.append( len(nums) )

        return missingNum
