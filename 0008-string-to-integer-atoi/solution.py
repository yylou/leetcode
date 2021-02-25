class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        ##  question: would input be like '12 and 34'?                     -> Yes, and stop at 'a'
        ##  question: would sign value shows up repeatedly? (e.g., '+-12') -> Yes, and return 0

        integer = []
        sign    = ''

        for char in s :
            ##  (skip case) ignore leading whitespace
            if sign == '' and len( integer ) == 0 and char == ' ' : continue

            ##  (end cass) duplicate sign char
            if ( char == '-' or char == '+' ) and sign != '': break

            ##  record the first '-' or '+' only when no digit or sign is read
            if ( char == '-' or char == '+' ) and sign == '' and len( integer ) == 0 : sign = char

            ##  break if char is non-digit
            elif not char.isdigit() : break

            else : integer.append( char )

        if len( integer ) == 0 : return 0

        value = int( ''.join( integer ) )
        if sign == '-' : value *= -1

        if   value < -2**31    : return -2**31
        elif value >  2**31 -1 : return  2**31 - 1

        return value
