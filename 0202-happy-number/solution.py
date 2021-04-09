class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        #:  (edge case)
        if n == 1: return True
        if n < 4: return False


        def calculate( num ):
            result = 0
            while num:
                remain = num % 10
                num /= 10
                result += remain*remain
            return result


        #:  Solution (1) using hash table to record
        #:  - time complexity: O(n)
        #:  - space complexity: O(n)
        record = set()
        while True:
            n = calculate(n)
            if n == 1: return True
            if n in record: return False
            record.add(n)


        # ============================================================ #


        #:  Solution (2) Floyd's Cycle-Finding Algorithm
        #:  - time complexity: O(logn)
        #:  - space complexity: O(1)
        slowP, fastP = n, calculate(n)
        while fastP != 1 and slowP != fastP:
            slowP = calculate(slowP)
            fastP = calculate(calculate(fastP))
        return fastP == 1
