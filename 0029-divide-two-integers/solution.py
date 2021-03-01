class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        ##  check whether answer is negative or positive
        positive = (dividend < 0) is (divisor < 0)

        ##  already got the sign of final answer, we could ABS the input integer
        dividend, divisor = abs(dividend), abs(divisor)

        ret_value, iteration = 0, 0

        ##  record the number of iterations (i.e., dividend >= divisor*2 for n times)
        while dividend >= (divisor << iteration) :
            iteration += 1

        for i in range( iteration )[::-1] :
            ##  condition of the end of for loop
            if dividend < divisor : break

            ##  one iteration = dividend - divisor *2 for i times
            if dividend >= (divisor << i) :
                dividend -= divisor << i

                ##  return value is also added by '1 << i'
                ret_value += 1 << i

        ##  adding back the right sign for the final answer
        if not positive : ret_value *= -1

        ##  make sure return value is in the correct range
        return min( max(-2147483648, ret_value), 2147483647 )
