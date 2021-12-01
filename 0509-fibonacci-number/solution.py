class Solution:
    def fib(self, n: int) -> int:
        # (base case)
        if n == 0 or n == 1: return n

        # ==================================================
        #  Dynamic Programming                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        n1, n2 = 0, 1
        for i in range(n - 1):
            n1, n2 = n2, n1 + n2

        return n2
