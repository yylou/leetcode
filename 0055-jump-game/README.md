# Problem
[55. Jump Game](https://leetcode.com/problems/jump-game/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # (base case)
        if len(nums) == 1: return True
        if nums[0] == 0: return False
        
        # ==================================================
        #  Greedy + Dynamic Programming                    =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        prevIndex = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= prevIndex: prevIndex = i
                
        return prevIndex == 0
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean canJump(int[] nums) {
        /* base case */
        if(nums.length == 1) return true;
        if(nums[0] == 0) return false;
        
        boolean dp[] = new boolean[nums.length];
        dp[nums.length - 1]=true;
        
        int cur = nums.length - 1;
        for(int i=nums.length-2 ; i>=0 ; i--) {
            if(i + nums[i] >= cur){
                dp[i] = true;
                cur = i;
            }
        }
        
        return dp[0];
    }
}
```