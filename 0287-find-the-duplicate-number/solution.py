class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##  Solution (1) Floyd's algorithm
        ##  - time complexity: O(n)
        ##  - space complexity: O(1)
        fastP, slowP = nums[0], nums[0]

        ##  (1) reach the intersection
        while True:
            slowP = nums[slowP]
            fastP = nums[nums[fastP]]
            if slowP == fastP: break

        ##  (2) find the entrance of the cycle
        slowP = nums[0]
        while slowP != fastP:
            slowP = nums[slowP]
            fastP = nums[fastP]

        return slowP


        # ============================================================================= #


        ##  Solution (2) 2-pass scan to convert numbers to NEGATIVE as unique number
        ##  - time complexity: O(n)
        ##  - space complexity: O(1), but modifiy the input list 'nums'
        n = len( nums )
        for i in xrange( n ):
            curVal = abs( nums[i] )

            if nums[curVal] < 0: return curVal
            else: nums[curVal] *= -1


        # ============================================================================= #


        ##  Solution (3) using set to record unique numbers
        ##  - time complexity: O(n)
        ##  - space complexity: O(n)
        unique = set()
        for element in nums:
            if element not in unique: unique.add( element )
            else: return element
