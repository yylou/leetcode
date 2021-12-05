class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public int[] findErrorNums(int[] nums) {
        int dup = 0, mis = 0;
        
        for(int num: nums) {
            int index = Math.abs(num) - 1;
            
            if(nums[index] < 0) dup = Math.abs(num);
            else nums[index] *= -1;
        }
        
        for(int i=0 ; i<nums.length ; i++) {
            if(nums[i] > 0) mis = i+1;
        }
        
        return new int[] {dup, mis};
    }
}
