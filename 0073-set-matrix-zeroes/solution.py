class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix[0])
        y = len(matrix)


        #:  Solution (1) in-place replacement
        #:  - time complexity: O(m*n) [multiple-pass]
        #:  - space complexity: O(1)
        col, row = False, False
        for i in xrange( y ):
            for j in xrange( x ):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

                    #:  using two flags to indicate whether first row and col need to be ZERO
                    if i == 0: row = True
                    if j == 0: col = True

        for i in xrange( 1, y ):
            for j in xrange( 1, x ):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row:
            matrix[0] = [0] * x
        if col:
            for i in xrange( y ): matrix[i][0] = 0


        # ============================================================================ #


        """
        #:  Solution (2) using O(m+n) space to record the index of '0' element
        #:  - time complexity: O(m*n) [two-pass]
        #:  - space complexity: O(m+n)
        setX = set()
        setY = set()

        for i in xrange( y ):
            for j in xrange( x ):
                if matrix[i][j] == 0:
                    setX.add( j )
                    setY.add( i )

        for i in xrange( y ):
            for j in xrange( x ):
                if i in setY or j in setX:
                    matrix[i][j] = 0
        """
