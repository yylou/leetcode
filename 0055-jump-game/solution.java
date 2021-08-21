class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean canJump(int[] nums) {
        /* base case */
        if(nums.length == 1) return true;
        if(nums[0] == 0) return false;
        
        boolean dp[] = new boolean[nums.length];
        dp[nums.length - 1]=true;
        
        int cur = nums.length - 1;
        for(int i=nums.length-2 ; i>=0 ; i--) {
            if(i + nums[i] >= cur){
                dp[i] = true;
                cur = i;
            }
        }
        
        return dp[0];
    }
}