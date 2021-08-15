class Solution:
    def reverse(self, x: int) -> int:
        # (base case)
        if x == 0: return x
        
        # ==================================================
        #  Math                                            =
        # ==================================================
        # time  : O(log(n))
        # space : O(1)
        
        ans  = 0
        sign = 1 if x > 0 else -1
        x    = abs(x)
        
        while x:
            pop = x % 10
            x //= 10
            
            ans = ans*10 + pop
            if ans >= 2**31-1: return 0
            
        return sign * ans