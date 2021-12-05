# Problem
[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # (base case)
        if len(nums) == 1: return False
        
        # ==================================================
        #  One-liner                                       =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        return len(nums) != len(set(nums))
```

```Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # (base case)
        if len(nums) == 1: return False
        
        # ==================================================
        #  Array + Set                                     =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        table = set()
        
        for num in nums:
            if num not in table: table.add(num)
            else: return True
        
        return False
```

```Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # (base case)
        if len(nums) == 1: return False
        
        # ==================================================
        #  Quick Sort                                      =
        # ==================================================
        # time  : O(nlogn)
        # space : O(logn)
        
        sorted_array = self.quickSort(nums)
        for i in range(0, len(sorted_array)-1):
            if sorted_array[i] == sorted_array[i+1]: return True
        return False

    def quickSort(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1: return nums
        
        pivot = nums[len(nums) // 2]
        lt, eq, lg = list(), list(), list()
        for num in nums:
            if   num == pivot: eq += [num]
            elif num  > pivot: lg += [num]
            else: lt += [num]
                
        return self.quickSort(lt) + eq + self.quickSort(lg)
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        
        for (int x: nums) {
            if (set.contains(x)) return true;
            set.add(x);
        }
        
        return false;
    }
}
```
