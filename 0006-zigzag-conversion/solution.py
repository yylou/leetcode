##  visit by row
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        length = len( s )

        ##  (edge case) numRows = 1, row > length of string
        if numRows == 1 : return s
        if numRows >= length : return s

        ##  calculate the divide unit
        gap = numRows - 2
        cycle = numRows + gap

        record = ''

        for i in range( numRows ) :
            j = 0
            while j+i < length :
                ##  EDGE elements
                record += s[j + i]

                ##  INNER elements (not first/last row)
                if i != 0 and i != numRows - 1 and j + cycle - i < length :
                    record += s[j + cycle - i]

                j += cycle

        return record
