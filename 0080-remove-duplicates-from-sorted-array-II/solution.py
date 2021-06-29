class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #  (base case)
        if len(nums) == 1 or len(nums) == 2: return len(nums)
        
        # ==================================================
        #  Array + Two Pointer                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        placeP, moveP = 0, 0
        
        while moveP < len(nums):
            num = nums[moveP]
            
            if placeP < 2 or num != nums[placeP - 2]:
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
        if(nums.length == 1 || nums.length == 2) return nums.length;
        
        int moveP = 0, placeP = 0;
        
        while(moveP < nums.length) {
            int num = nums[moveP];
            
            if(placeP < 2 || num != nums[placeP - 2]) {
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
