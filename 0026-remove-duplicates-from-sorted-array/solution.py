class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #  (base case)
        if len(nums) == 0 or len(nums) == 1: return
        
        # ==================================================
        #  Array + Two Pointer                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        moveP, placeP = 0, 0
        
        while moveP < len(nums):
            num = nums[moveP]
            
            #  (meet number different from previous placed number)
            if placeP < 1 or num != nums[placeP - 1]:
                nums[placeP] = num
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
==================================================================================================
'''
