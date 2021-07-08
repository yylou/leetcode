class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public void moveZeroes(int[] nums) {
        /* base case */
        if(nums.length == 1) return;
        
        int moveP = 0, placeP = 0;
        
        while(moveP < nums.length) {
            if(nums[moveP] != 0) {
                /* swap */
                int tmp = nums[placeP];
                nums[placeP] = nums[moveP];
                nums[moveP] = tmp;
                
                placeP += 1;
            }
            
            moveP += 1;
        }
    }
}
