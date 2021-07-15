class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # (base case)
        if len(nums) == 1: return nums[0]
        
        # ==================================================
        #  Array + Dynamic Programming                     =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        curSum = maxSum = nums[0]
        
        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(curSum, maxSum)

        return maxSum
    
        '''
        # ==================================================
        #  Array + Dynamic Programming + Greedy            =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        dp = [None] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            ##  to determine local MAX, choose between accumulating or restart at the next number
            ##  - (example) [-2, 1, 2], it is clear that sum of (-2+1) is smaller than '1'
            ##                          so restart at '1' would be the next action
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            
        return max(dp)
        '''