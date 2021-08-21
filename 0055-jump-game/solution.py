class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # (base case)
        if len(nums) == 1: return True
        if nums[0] == 0: return False
        
        # ==================================================
        #  Greedy                                          =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        prevIndex = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= prevIndex: prevIndex = i
                
        return prevIndex == 0

        '''
        # ==================================================
        #  Dynamic Programming                             =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        dp = [False] * len(nums)
        dp[-1] = True
        
        cur = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= cur:
                dp[i] = True
                cur = i
        
        return dp[0] == True
        '''