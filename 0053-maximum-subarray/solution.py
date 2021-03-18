class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##  (edge case) length == 1
        if len(nums) == 1: return nums[0]


        ##  Solution (1) Greedy
        localMax = globalMax = nums[0]
        for i in xrange( 1, len(nums) ):
            ##  to determine local MAX, choose between accumulating or restart at the next number
            ##  - (example) [-2, 1, 2], it is clear that sum of (-2+1) is smaller than '1'
            ##                          so restart at '1' would be the next action
            localMax = max( nums[i], localMax + nums[i] )

            globalMax = max( localMax, globalMax )

        return globalMax


        # ======================================================================================= #

        ##  Solution (2) Divide and Conquer (follow LeetCode Solution)
        mid = len(nums) // 2

        leftSum  = self.maxSubArray( nums[:mid] )
        rightSum = self.maxSubArray( nums[mid:] )
        midSum   = self.crossSum( nums, mid )

        return max( leftSum, rightSum, midSum )


    def crossSum(self, nums, mid):
        leftSum = rightSum = float( '-inf' )
        tmpSum = 0

        ##  (1) Left Part
        for i in xrange( mid-1, -1, -1 ):
            tmpSum += nums[i]
            leftSum = max( tmpSum, leftSum )

        tmpSum = 0

        ##  (2) Right Part
        for i in xrange( mid, len(nums) ):
            tmpSum += nums[i]
            rightSum = max( tmpSum, rightSum )

        return leftSum + rightSum
