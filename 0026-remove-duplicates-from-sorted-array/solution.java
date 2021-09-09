class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public int removeDuplicates(int[] nums) {
        /* base case */
        if(nums.length == 0 || nums.length == 1) return nums.length;
        
        int moveP = 0, placeP = 0;
        
        while(moveP < nums.length) {
            int num = nums[moveP];
            
            if(placeP < 1 || num != nums[placeP - 1]) {
                nums[placeP] = num;
                placeP += 1;
            }
            
            moveP += 1;
        }
        
        return placeP;
    }
}