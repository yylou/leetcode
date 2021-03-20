class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        ##  (edge case) k sliding windows / 1 sliding windows
        n = len(nums)
        if k == 1: return nums
        if k == n: return [max(nums)]


        ##  Solution (1) dynamic programming
        leftMax, rightMax = [nums[0]] + ['']*(n-1), ['']*(n-1) + [nums[-1]]

        ##  (a) build local-max array from left-to-right and right-to-left
        for i in xrange( 1, n ):
            lIndex = i
            rIndex = n-i-1

            if lIndex % k == 0: leftMax[lIndex] = nums[lIndex]
            else: leftMax[lIndex] = max( nums[lIndex], leftMax[lIndex-1] )

            if (rIndex+1) % k == 0: rightMax[rIndex] = nums[rIndex]
            else: rightMax[rIndex] = max( nums[rIndex], rightMax[rIndex+1] )

        ##  (b) build the answer by comparing 2 local-max arrays
        answer = [''] * (n-k+1)
        for i in xrange( n-k+1 ):
            if i % k == 0: answer[i] = leftMax[i+k-1]
            else: answer[i] = max( rightMax[i], leftMax[i+k-1] )

        return answer


        # ===================================================================================== #


        ##  Solution (2) using 'queue' to record previous MAX element and the following elements
        stack = []
        for i in xrange( k ):
            ##  remove the elements which are smaller than the next element
            while stack and nums[i] > nums[stack[-1]]: stack.pop()
            stack.append( i )

            # print 'start ', map( lambda x: nums[x], stack)

        answer = []
        for i in xrange( k-1, n ):
            ##  remove the elements which are smaller than the next element
            while stack and nums[i] > nums[stack[-1]]: stack.pop()
            stack.append( i )

            # print 'before', map( lambda x: nums[x], stack)

            ##  before appending the MAX element, remove elements in stack which are out-of-range
            while i - stack[0] >= k: stack.pop(0)

            # print 'remove', map( lambda x: nums[x], stack)

            answer.append( nums[stack[0]] )

        return answer
