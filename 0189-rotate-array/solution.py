class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len( nums )

        ##  no need any action when
        ##  (1) length == 1
        ##  (2) the number of rotates is the multiplication of length
        if length > 1 and k % length != 0:

            ##  Solution (1) Cyclic Replacements
            ##  - extra space complexity: O(1), only constant variable
            rotateNum = k % length
            start, replaceCounter = 0, 0

            while replaceCounter < length:
                curIndex, oriElement = start, nums[start]
                while True:
                    ##  replace according to the rotate times, record ORIGINAL element
                    nextIndex = (curIndex + rotateNum) % length
                    nums[nextIndex], oriElement = oriElement, nums[nextIndex]
                    curIndex = nextIndex

                    ##  counting the replace times
                    replaceCounter += 1

                    ##  BREAK condition: got back to the original location
                    if start == curIndex: break

                start += 1

            return

            # ========================================================================== #

            ##  Solution (2) extend the original array and reassign the element
            ##  - extra space complexity: O(n)
            rotateNum = k % length
            nums *= 2
            nums[:] = nums[length-rotateNum:length*2-rotateNum]
