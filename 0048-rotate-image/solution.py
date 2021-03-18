class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        ##  (edge case)
        if len(matrix) == 1: return matrix

        ##  Test cases:
        ##    [[1,2,3],[4,5,6],[7,8,9]]
        ##    [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        ##    [[5,1,9,11,17],[2,4,8,10,18],[13,3,6,7,19],[15,14,12,16,20],[21,22,23,24,25]]

        iteration = len( matrix ) // 2 + len( matrix ) % 2

        for i in range( iteration ):
            for j in range( i, len( matrix )-1-i ):
                # stack = [matrix[i][j], matrix[j][i*-1-1], matrix[i*-1-1][j*-1-1], matrix[j*-1-1][i]]

                tmpVal                 = matrix[j*-1-1][i]
                matrix[j*-1-1][i]      = matrix[i*-1-1][j*-1-1]
                matrix[i*-1-1][j*-1-1] = matrix[j][i*-1-1]
                matrix[j][i*-1-1]      = matrix[i][j]
                matrix[i][j]           = tmpVal
