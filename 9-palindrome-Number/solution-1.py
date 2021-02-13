##  differentiate odd and even integer to do string reverse
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ##  edge case handling: [1-9]
        if x < 0 : return False
        if x < 10 : return True

        str_num = str( x )
        length = len( str_num )

        ##  even integer
        if length % 2 == 0 :
            return True if str_num[:length/2] == str_num[length/2:][::-1] else False

        ##  odd integer
        else :
            return True if str_num[:length/2] == str_num[length/2+1:][::-1] else False
