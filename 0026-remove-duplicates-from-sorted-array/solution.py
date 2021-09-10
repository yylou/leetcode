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