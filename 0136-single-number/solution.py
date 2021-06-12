class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #: (base case)
        if len(nums) == 1: return nums[0]
        
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
    
        '''
        # ==================================================
        #  Bit Manipulation                                =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        # 0^a = a so the initial value of ret can be 0
        ret = 0
        for num in nums: ret ^= num
        return ret
        
        # ==================================================
        #  Math                                            =
        # ==================================================
        # time  : O(n+n+n) for set(nums) and sum operations
        # space : O(n)     for set(nums)
        
        return 2 * sum(set(nums)) - sum(nums)
        '''
        
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int singleNumber(int[] nums) {
        int ret = 0;
        for(int num : nums){
            ret ^= num;
        }
        return ret;
    }
==================================================================================================
'''
