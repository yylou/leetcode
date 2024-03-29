# Problem
[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # (base case)
        if len(nums) == 0 or len(nums) == 1: return len(nums)
        
        # ==================================================
        #  Array + Two Pointer                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        moveP, placeP = 0, 0
        
        while moveP < len(nums):
            # meet number different from previous placed number
            if placeP == 0 or nums[moveP] != nums[placeP - 1]:
                nums[placeP] = nums[moveP]
                placeP += 1
                
            moveP += 1
        
        return placeP
```

# Java
```Java
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
```
