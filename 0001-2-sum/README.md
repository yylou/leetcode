# Problem
[1. Two Sum](https://leetcode.com/problems/two-sum/)

# Performance
![result](./result.png)

# Python
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # ==================================================
        #  Array + Hash Table                              =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        table = dict()
        for i in range(len(nums)):
            remain = target - nums[i]

            if remain in table:
                return [i, table[remain]]

            # We could overwrite since there is only one solution
            table[nums[i]] = i
```
            
# Java
```Java
class Solution {
    /**  
     * @time  : O(n)
     * @space : O(n)
     */
    
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i=0 ; i<nums.length ; i++) {
            int remain = target - nums[i];
            if(map.containsKey(remain)) return new int[] {i, map.get(remain)};
            
            map.put(nums[i], i);
        }
        
        return null;
    }
}
```
