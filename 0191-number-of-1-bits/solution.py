class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # ==================================================
        #  Bit Manipulation                                =
        # ==================================================
        # time  : O(1)
        # space : O(1)
        
        ans = 0
        
        while n:
            # remove the rightmost in binary representation of n
            n &= (n-1)
            ans += 1
            
        return ans
        
        '''
        # ==================================================
        #  Math                                            =
        # ==================================================
        # time  : O(1)
        # space : O(1)
        
        ans = 0
        
        while n:
            if n & 1: ans += 1
            n >>= 1
            
        return ans
        '''