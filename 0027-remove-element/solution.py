class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        length = len( nums )

        ##  (edge case) empty list
        if length == 0 : return 0

        ##  counter to record unequal element
        retVal = 0

        for i in range( length ) :
            ##  meet the unequal element
            ##  --> assign to the array by a counter (retVal), which is the return value
            if nums[i] != val :
                nums[retVal] = nums[i]
                retVal += 1

        return retVal
