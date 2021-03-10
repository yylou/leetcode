class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        pCur, pIndexToBePlace = 0, 0

        while pCur < len( nums ):
            if nums[pCur] != 0:
                ##  (1) whenever meet NON-ZERO element, move it forward
                if nums[pIndexToBePlace] != nums[pCur]:
                    nums[pIndexToBePlace], nums[pCur] = nums[pCur], nums[pIndexToBePlace]

                ##  (2) move the pointer that points to the index to be placed by NON-ZERO element
                pIndexToBePlace += 1

            pCur += 1
