class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #  (base case)
        if len(nums) == 1: return
        
        # ==================================================
        #  Array + Two Pointer                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        placeP, moveP = 0, 0
        
        while moveP < len(nums):
            if nums[moveP] != 0: 
                nums[placeP], nums[moveP] = nums[moveP], nums[placeP]    
                placeP += 1
            
            moveP += 1
