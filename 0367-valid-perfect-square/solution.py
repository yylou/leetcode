class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # (base case)
        if num == 1: return 1
        
        # ==================================================
        #  Array + Binary Search                           =
        # ==================================================
        # time  : O(log(n))
        # space : O(1)
        
        l, r = 0, num
        while l < r:
            mid = (l + r) // 2
            val = mid * mid
            
            if val == num: return True
            elif val > num: r = mid
            elif val < num: l = mid + 1
            
        return False