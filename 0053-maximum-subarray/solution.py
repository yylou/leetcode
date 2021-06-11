class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #: (edge case)
        if len(nums) == 1: return nums[0]
        
        # ==================================================
        #  Array + Dynamic Programming + Greedy            =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        dp = [None] * len(nums)
        dp[0] = nums[0]
        
        for i in range( 1, len(nums) ):
            ##  to determine local MAX, choose between accumulating or restart at the next number
            ##  - (example) [-2, 1, 2], it is clear that sum of (-2+1) is smaller than '1'
            ##                          so restart at '1' would be the next action
            dp[i] = max( nums[i], dp[i-1] + nums[i] )
            
        return max(dp)
    
        '''
        # ==================================================
        #  Array + Dynamic Programming + Greedy            =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        localMax = globalMax = nums[0]
        
        for i in xrange( 1, len(nums) ):
            localMax = max( nums[i], localMax + nums[i] )
            globalMax = max( localMax, globalMax )

        return globalMax
        '''
        
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int maxSubArray(int[] nums) {
        int localMax = nums[0], globalMax = nums[0];
        
        for( int i=1 ; i<nums.length ; i++){
            localMax  = Math.max(nums[i], localMax + nums[i]);
            globalMax = Math.max(localMax, globalMax);
        }
        
        return globalMax;
    }
}
==================================================================================================
'''
