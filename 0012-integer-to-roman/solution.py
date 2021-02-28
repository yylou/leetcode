##  mathematical solution
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map_table = {1:    'I',
                     5:    'V',
                     10:   'X',
                     50:   'L',
                     100:  'C',
                     500:  'D',
                     1000: 'M'}

        retVal = ""

        iterative = sorted( map_table.keys(), reverse=True )

        for key, value in enumerate( iterative ):
            if num >= value:
                scale, strNum = int( num / value ), str( num )

                ##  4: current char - previous char (e.g., 40: 50 - 10 = XL)
                if strNum[0] == '4' :
                    retVal += map_table[value] + map_table[iterative[key-1]]
                    num -= scale * value

                ##  9: next char - previous char (e.g., 900: 1000 - 100 = CM)
                elif strNum[0] == '9' :
                    retVal += map_table[iterative[key+1]] + map_table[iterative[key-1]]
                    num -= 9 * 10 ** ( len( strNum ) -1 )

                else:
                    retVal += map_table[value] * scale
                    num -= value * scale

        return retVal
