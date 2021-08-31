class Solution:
    def tribonacci(self, n: int) -> int:
        # (base case)
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        
        # ==================================================
        #  Dynamic Programming                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        first, second, third = 0, 1, 1
        
        for i in range(n - 2):
            ans = first + second + third
            first = second
            second = third
            third = ans
            
        return third