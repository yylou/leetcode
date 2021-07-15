class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int maxSubArray(int[] nums) {
        int curSum = nums[0], maxSum = nums[0];
        
        for(int i=1 ; i<nums.length ; i++){
            curSum = Math.max(nums[i], curSum + nums[i]);
            maxSum = Math.max(curSum, maxSum);
        }
        
        return maxSum;
    }
}