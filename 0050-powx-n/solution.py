class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        ##  (edge case) x == 1 or 2
        if x == 1: return 1
        if x == 2 and n > 0:
            answer = 1
            for i in range( n ): answer = answer << 1
            return answer

        ##  (condition) n is negatie
        if n < 0:
            x = 1 / x
            n = -n

        """
        (example) x^10 = x^2*x^8
        1st iteration: answer = 1,    product2 = x^2, n = 5
        2nd iteration: answer = x^2,  product2 = x^4, n = 2
        3rd iteration: answer = x^2,  product2 = x^8, n = 1
        4th iteration: answer = x^10, product2 = x^16, n = 0

        (example) x^7 = x^3*x^4
        1st iteration: answer = x,   product2 = x^2, n = 3
        2nd iteration: answer = x^3, product2 = x^4, n = 1
        3rd iteration: answer = x^7, product2 = x^8, n = 0
        """

        answer, product2 = 1, x
        while n > 0:
            ##  do single mutiplication on the 'answer' so that 'product2' would not be affected
            if n % 2 != 0: answer = answer * product2
            product2 *= product2

            n //= 2

        return answer
