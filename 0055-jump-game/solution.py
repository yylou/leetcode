class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        ##  (edge case) length == 1 / 1st element == 0
        if len(nums) == 1: return True
        if nums[0] == 0: return False


        ##  Solution (1) greedy (from backward)
        n = len(nums)
        prevIndex = n-1
        for i in xrange( n-1, -1, -1 ):
            if i+nums[i] >= prevIndex: prevIndex = i

        return prevIndex == 0


        # ============================================================================== #


        ##  Solution (2) dynamic programming (bottom-up) == Time Limit Exceeded
        n = len(nums)
        memo = ['']*(n-1) + ['g']


        for i in xrange( n-2, -1, -1 ):
            ##  REACH / BEYOND the destination, reutrn
            if i+1+nums[i] >= n: memo[i] = 'g'
            else:
                for j in xrange( i, i+nums[i]+1 ):
                    if memo[j] == 'g':
                        memo[i] = 'g'
                        break

        return memo[0] == 'g'


        # ============================================================================== #


        ##  Solution (3) dynamic programming (top-down) == Time Limit Exceeded
        n = len(nums)
        memo = ['']*(n-1) + ['g']


        def jump( index ):
            if memo[index]: return True if memo[index] == 'g' else False

            for i in xrange( nums[index], 0, -1 ):
                ##  REACH / BEYOND the destination, reutrn
                if index+i >= n: return True

                if jump( index+i ):
                    memo[index] = 'g'
                    return True

            memo[index] = 'b'
            return False


        return jump( 0 )


        # ============================================================================== #


        ##  Solution (4) brute-force, trying each possible move == Time Limit Exceeded
        for i in xrange( nums[0], 0, -1 ):
            if i < len(nums):
                if self.canJump( nums[i:] ): return True

        return False
