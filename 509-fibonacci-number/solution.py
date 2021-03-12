class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 : return 0
        if n == 1 or n == 2 : return 1

        ##  Dynamic Programming (bottom-up) Time: O(N)
        ##  - Only record 2 of the previous results, Space: O(1)
        pre = 1
        cur = 1
        for i in range( 3, n+1 ) :
            sum = pre + cur
            pre = cur
            cur = sum
        return cur

        # ====================================================== #

        ##  Brute Force Solution: O(2^N)
        return self.fib(n-1) + self.fib(n-2)

'''
# =====================================================
#  Dynamic Programming (top-down)                     =
# =====================================================
class Solution(object):
    def __init__( self ) :
        self.dp_table = {0: 0, 1: 1, 2: 1}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dp_table: return self.dp_table[n]

        val1, val2 = self.fib(n-1), self.fib(n-2)
        if n-1 not in self.dp_table : self.dp_table[n-1] = val1
        if n-2 not in self.dp_table : self.dp_table[n-2] = val2

        return val1 + val2

# =====================================================
#  Dynamic Programming (bottom-up)                    =
# =====================================================
class Solution(object):
    def __init__(self) :
        self.dp_table = {0: 0, 1: 1, 2: 1}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dp_table : return self.dp_table[n]
        else :
            for i in range( 3, n+1 ) :
                self.dp_table[i] = self.dp_table[i-1] + self.dp_table[i-2]
            return self.dp_table[n]
'''
