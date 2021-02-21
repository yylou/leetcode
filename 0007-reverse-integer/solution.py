class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strX = list( str( abs(x) ) )

        ##  two pointers solution: convert integer to list of string, and SWAP element
        left, right = 0, len(strX)-1
        while right > left :
            strX[left], strX[right] = strX[right], strX[left]

            left  += 1
            right -= 1

        ##  NEGATIVE or POSITIVE
        if x < 0 : retVal = int( ''.join(strX) ) * -1
        else : retVal = int( ''.join(strX)  )

        ##  range checking
        if retVal >= 2**31-1 or retVal <= -2**31: return 0
        else : return retVal
