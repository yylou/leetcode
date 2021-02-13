##  mathematical solution: divide input number and use mod operation to get the reversed number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ##  edge case handling: [1-9], 10/100/1000/..
        if x < 0 : return False
        if x < 10 : return True
        if x != 0 and x % 10 == 0 : return False

        ##  Example: 323
        ##    (1st iteration) ret_value = 3,  x = 32
        ##    (2nd iteration) ret_value = 32, x = 3   -> end of while loop
        ##
        ##  Example: 5445
        ##    (1st iteration) ret_value = 5,  x = 544
        ##    (2nd iteration) ret_value = 54, x = 54  -> end of while loop
        ret_value = 0
        while x > ret_value :
            ret_value = ret_value * 10 + x % 10
            x /= 10

        ##  Odd  length: x == ret_value/10
        ##  Even length: x == ret_value
        return True if x == ret_value or x == ret_value/10 else False
