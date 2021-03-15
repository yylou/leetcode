class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        ##  (edge case) x is smaller than 2
        if x < 2: return x

        ##  Solution (1) Binary search
        left, right = 2, x//2
        while left <= right:
            mid = (left + right) // 2

            if x == mid*mid: return mid

            if x > mid*mid: left = mid+1
            else: right = mid-1

        return right


        # ======================================================== #


        ##  Solution (2) One-liner with Python built-in function
        return int( sqrt(x) )
