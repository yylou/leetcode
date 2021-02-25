class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##  (edge case) empty list of integers
        if not nums : return 0

        length = len( nums )

        if length == 1 : return 1

        ##  using this index to flag the last unique element (also the index to put new integer)
        uniqueIndex = 0

        for i in range( length ) :
            ##  (1) assign the unique element to the array by the current index
            ##      since the system checks the answer by printing via the return index, pop or delete is not necessary
            ##  (2) skip the duplicate element and the next iteration would overwrite the one
            if nums[i] != nums[uniqueIndex] :
                uniqueIndex += 1
                nums[uniqueIndex] = nums[i]

        return uniqueIndex + 1
