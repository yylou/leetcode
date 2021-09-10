class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # (base case)
        if len(nums) == 1: return nums[0]

        # ==================================================
        #  Bit Manipulation                                =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        # a^0 = a, a^a = 0, a^a^b = 0^b
        ret = 0
        for num in nums: ret ^= num
        return ret
    
        '''
        # ==================================================
        #  Python Set                                      =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        record = set()
        for num in nums:
            if num in record: record.remove(num)
            else: record.add(num)
        return record.pop()
        
        # ==================================================
        #  Math                                            =
        # ==================================================
        # time  : O(n+n) for set(nums) and sum operations
        # space : O(n)   for set(nums)
        
        # 2 * (a+b+c) − (a+a+b+b+c) = c
        return 2 * sum(set(nums)) - sum(nums)
        '''