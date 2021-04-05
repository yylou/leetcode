class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #:  (edge case) length == 1
        n = len(nums)
        if n == 1: return

        #:  NOTE: index to PLACE '0' or '2'
        zeroP, twoP = 0, n-1

        #:  move pointer for '2' until meet non-2 element, check whether all numbers are '2'
        while twoP >= 0 and nums[twoP] == 2: twoP -= 1
        if twoP == 0: return

        #:  move pointer for '0' until meet non-0 element, check whether all numbers are '0'
        while zeroP < n and nums[zeroP] == 0: zeroP += 1
        if zeroP == n: return

        #:  'nums' does not have '1'
        if twoP == zeroP: return

        curP = zeroP

        while curP <= twoP:
            if nums[curP] == 0:
                nums[curP], nums[zeroP] = nums[zeroP], nums[curP]
                zeroP += 1
                curP += 1

            #:  meet '2', cur pointer stays in order to check whether swapped elemnt is '0'
            elif nums[curP] == 2:
                nums[curP], nums[twoP] = nums[twoP], nums[curP]
                twoP -= 1

            else:
                curP += 1
