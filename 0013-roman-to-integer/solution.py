##  mathematical solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_table = { 'I'  :    1,
                      'V'  :    5,
                      'X'  :   10,
                      'L'  :   50,
                      'C'  :  100,
                      'D'  :  500,
                      'M'  : 1000  }

        ##  (edge case) input already in the table
        if len( s ) == 1 : return map_table[s]

        retVal = 0
        curType = 1000

        for char in s :
            value = map_table[char]

            retVal += value

            ##  if previous char mapped to smaller value (compared with current char)
            ##  subtract the mapped value * 2
            if value > curType : retVal -= curType * 2

            curType = value

        return retVal
