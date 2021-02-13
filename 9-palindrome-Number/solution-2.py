##  mathematical solution: divide input number and use mod operation to get the reversed number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ## edge case handling: [1-9]
        if x < 0 : return False
        if x < 10 : return True
        if x != 0 and x % 10 == 0 : return False

        ret_value = 0
        while x > ret_value :
            ret_value = ret_value * 10 + x % 10
            x /= 10

        return True if x == ret_value or x == ret_value / 10 else False
