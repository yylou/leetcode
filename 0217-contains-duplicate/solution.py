class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1: return False

        #:  Solution (1) one-liner by using SET
        return True if len( set(nums) ) < n else False


        # ======================================================== #


        #:  Solution (2) iterative
        record = set()
        for element in nums:
            if element in record: return True
            record.add( element )
        return False
