# Problem
[75. Sort Colors](https://leetcode.com/problems/sort-colors)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #: (base case)
        if len(nums) == 1: return
        
        # ==================================================
        #  Array + Three Pointers                          =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        p0, p2 = 0, len(nums)-1
        
        #: move pointer for '0' until meet non-0 element, check whether all numbers are '0'
        while p0 < len(nums) and nums[p0] == 0: p0 += 1
        if p0 == len(nums): return
        
        #: move pointer for '2' until meet non-2 element, check whether all numbers are '2'
        while p2 >= 0 and nums[p2] == 2: p2 -= 1
        if p2 == 0: return
        
        moveP = p0
        
        while moveP <= p2:
            #: (ZERO)
            if nums[moveP] == 0:
                nums[moveP], nums[p0] = nums[p0], nums[moveP]
                
                p0 += 1
                moveP += 1
               
            #: (TWO)
            elif nums[moveP] == 2:
                nums[moveP], nums[p2] = nums[p2], nums[moveP]
                
                p2 -= 1
                
            #: (ONE)
            else: 
                moveP += 1
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    public void sortColors(int[] nums) {
        /* base case */
        if(nums.length == 1) return;
        
        int p0 = 0, p2 = nums.length - 1;
        
        while(p0 < p2 && nums[p0] == 0) p0++;
        if(p0 == p2) return;
            
        while(p2 <= 0 && nums[p2] == 2) p2--;
        if(p2 == 0) return;
            
        int moveP = p0;
        
        while(moveP <= p2) {
            if(nums[moveP] == 0) {
                int tmp = nums[p0];
                nums[p0] = nums[moveP];
                nums[moveP] = tmp;
                
                moveP++;
                p0++;
            } else if(nums[moveP] == 2) {
                int tmp = nums[p2];
                nums[p2] = nums[moveP];
                nums[moveP] = tmp;
                
                p2--;
            } else {
                moveP++;
            }
        }
    }
}
```
