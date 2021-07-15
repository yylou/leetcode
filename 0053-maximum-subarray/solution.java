class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int maxSubArray(int[] nums) {
        /* base case */
        if(nums.length == 1) return nums[0];
    
        int curSum = nums[0], maxSum = nums[0];
        
        for(int i=1 ; i<nums.length ; i++){
            curSum = Math.max(nums[i], curSum + nums[i]);
            maxSum = Math.max(curSum, maxSum);
        }
        
        return maxSum;
    }
}
