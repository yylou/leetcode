##  slight tweak from the problem '118. Pascal's Triangle'
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ##  edge case handling
        if rowIndex == 0 : return [1]
        if rowIndex == 1 : return [1, 1]
        if rowIndex == 2 : return [1, 2, 1]

        ret_value = [1, 2, 1]

        ##  'numRows - 2' times of iteration (since current ret_value is at rowIndex 2)
        for i in range( 0, rowIndex-2 ):

            ##  do the calculation BACKWARDS in order to replace the value without affecting the other calculation
            for j in range( len(ret_value)-1, 0, -1 ):
                ret_value[j] = ret_value[j] + ret_value[j-1]

            ret_value.append( 1 )

        return ret_value
