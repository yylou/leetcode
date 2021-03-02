class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ##  (edge case)
        if numRows == 0 : return []
        if numRows == 1 : return [[1]]
        if numRows == 2 : return [[1], [1, 1]]

        ret_value = [[1], [1, 1]]

        ##  iteration starts from the second element of ret_value, and then loop for 'numRows - 2' times
        for i in range( 1, numRows-1 ) :
            tmp_list = [1]

            ##  do the calculation of pairs of integers, then append into the temp list
            for j in range( 1, len(ret_value[i]) ) :
                tmp_list.append( ret_value[i][j] + ret_value[i][j-1] )

            tmp_list.append( 1 )

            ret_value.append( tmp_list )

        return ret_value
