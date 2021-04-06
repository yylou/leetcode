class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        x = len( grid[0] )
        y = len( grid )

        #:  (edge case) x == y == 1, y == 1
        if x == y == 1: return grid[0][0]


        #:  Solution (1) dynamic programming with 2D array memo
        pathRecord = [[0 for j in xrange(x)] for i in xrange(y)]
        pathRecord[0][0] = grid[0][0]

        for i in xrange( 1, x ): pathRecord[0][i] = pathRecord[0][i-1] + grid[0][i]
        if y == 1: return pathRecord[0][x-1]

        for i in xrange( 1, y ): pathRecord[i][0] = pathRecord[i-1][0] + grid[i][0]
        if x == 1: return pathRecord[y-1][0]

        for i in xrange( 1, y ):
            for j in xrange( 1, x ):
                pathRecord[i][j] = grid[i][j] + min( pathRecord[i-1][j], pathRecord[i][j-1] )

        return pathRecord[y-1][x-1]


        # ========================================================================================== #


        #:  Solution (2) dynamic programming without memo by modifying input 2D array
        x = len( grid[0] ) - 1
        y = len( grid ) - 1

        #:  (edge case) x == y == 1
        if x == y == 0: return grid[0][0]

        for yP in xrange( y, -1, -1 ):
            for xP in xrange( x, -1, -1 ):
                if   xP == x and yP != y: grid[yP][xP] += grid[yP+1][xP]
                elif xP != x and yP == y: grid[yP][xP] += grid[yP][xP+1]
                elif xP != x and yP != y: grid[yP][xP] += min( grid[yP+1][xP], grid[yP][xP+1] )

        return grid[0][0]
