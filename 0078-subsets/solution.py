class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []


        def recursive( subset, index ):
            if index > len(nums): return

            answer.append( subset )

            for i in xrange( index, len(nums) ):
                recursive( subset + [nums[i]], i+1 )


        recursive( [], 0 )
        return answer
