class Solution:
    def mySqrt(self, x: int) -> int:
        #: (edge)
        if x == 0: return 0
        if x < 4: return 1
        
        # ==================================================
        #  Binary Search + Math                            =
        # ==================================================
        # time  : O(log(n))
        # space : O(1)
        
        l, r = 0, x
        
        while l < r:
            mid = (l + r) // 2
            num = mid * mid
            
            if num == x: return mid
            elif num > x: r = mid
            elif num < x: l = mid + 1
                
        return l - 1
