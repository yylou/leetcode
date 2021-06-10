class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #:  (edge case)
        if len(nums) == 0 or ( len(nums) == 1 and nums[0] == val): return 0
        
        # ==================================================
        #  Array + Two Pointer                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        placeP, moveP = 0, 0
        
        while moveP < len(nums):
            if nums[moveP] != val:
                nums[placeP] = nums[moveP]
                placeP += 1
            
            moveP += 1
            
        return placeP
    
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public int removeElement(int[] nums, int val) {
        if( nums.length == 0 || (nums.length == 1 && nums[0] == val) ) return 0;
        
        int placeP = 0, moveP = 0;
        
        while( moveP < nums.length ){
            if( nums[moveP] != val ){
                nums[placeP++] = nums[moveP];
            }
            
            moveP++;
        }
        
        return placeP;
    }
}
==================================================================================================
'''
