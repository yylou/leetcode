class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        #:  (edge case)
        if num < 10: return num
        if num % 9 == 0: return 9


        #:  Solution (1) mathematical
        return num % 9


        # ========================================================= #


        #:  Solution (2) keep dividing and accumulating
        def calculate( num ):
            result = 0
            while num:
                remain = num % 10
                num /= 10
                result += remain
            return result

        while num > 9: num = calculate(num)
        return num
