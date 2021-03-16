class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##  (edge case) MAX value is smallen than 1
        if not nums: return 1


        ##  Solution (1) three-pass scan to CHECK and MODIFY 'nums'
        ##  - time complexity: O(n)
        ##  - space complexity: O(1)

        ##  [1st Scan]
        ##  - (1) Check the existence of '1'
        ##  - (2) for negative number and the number with value > length, turn them to '1'
        ONE = False
        length = len( nums )
        for i in xrange( length ):
            if not ONE and nums[i] == 1: ONE = True
            if nums[i] < 1 or nums[i] > length: nums[i] = 1

        ##  without '1', return 1 / with 1 but length == 1, return 2
        if not ONE: return 1
        if length == 1: return 2

        ##  [2nd Scan]
        ##  - mark the existence of number by ASSIGNING NEGATIVE value to certain index
        for i in xrange( length ):
            val = abs( nums[i] )

            if val == length: nums[0] = False
            else: nums[val] = -1 * abs( nums[val] )

        ##  [3rd Scan]
        ##  - return if the value is positive (string from '1' since '0' is to store LENGTH element)
        for i in xrange( 1, length ):
            if nums[i] > 0: return i

        ##  all pass but missing the one which value == length
        if nums[0] != False: return length

        ##  All numbers are consecutive, return length + 1
        return length + 1


        # ==================================================================================== #


        ##  Solution (2) using hash table to record positive numbers, and a counter for MIN value
        ##  - time complexity: O(n)
        ##  - space complexity: O(n)
        record = {}
        minVal = 1

        for num in nums:
            ##  FIND min value, using while loop to check the existence of consecutive numbers
            if num == minVal:
                minVal += 1
                while minVal in record:
                    minVal += 1

            ##  only record the number larger than current MIN value to save space
            if num > 0 and num > minVal:
                record[num] = record.get( num, 0 ) + 1

        return minVal


        # ==================================================================================== #


        ##  Solution (3) SORT at first, then iterate through the set to compare INDEX / VALUE
        ##  - time complexity: O(nlogn + n)
        ##  - space complexity: O(n)
        sortedArray = sorted( set([element for element in nums if element > 0]) )
        length = len(sortedArray)

        for i in range( length ):
            if i+1 != sortedArray[i]: return i+1

        return length+1
