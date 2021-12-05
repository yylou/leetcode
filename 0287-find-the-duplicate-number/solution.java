class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
     
    public int findDuplicate(int[] nums) {
        int slowP = nums[0], fastP = nums[0];
        
        while(true) {
            slowP = nums[slowP];
            fastP = nums[nums[fastP]];
            if(slowP == fastP) break;
        }
        
        slowP = nums[0];
        while(slowP != fastP) {
            slowP = nums[slowP];
            fastP = nums[fastP];
        }
        
        return slowP;
    }
}
