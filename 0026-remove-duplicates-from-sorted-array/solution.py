class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #  (base case)
        if len(nums) == 0 or len(nums) == 1: return len(nums)
        
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