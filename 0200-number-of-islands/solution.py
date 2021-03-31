class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        x = len(grid[0])
        y = len(grid)

        #:  (edge case)
        if x == y == 1: return 1 if grid[0][0] == '1' else 0


        #:  Solution (1) BFS
        #:  - time complexity: O(m*n)
        #:  - space complexity: O( min(m, n) )
        ans = 0
        for i in xrange( y ):
            for j in xrange( x ):
                if grid[i][j] == '1':
                    ans += 1

                    visited = set()
                    visited.add( (i, j) )

                    while visited:
                        index = visited.pop()
                        row = index[0]
                        col = index[1]
                        grid[row][col] = '0'

                        if row > 0   and grid[row-1][col] == '1': visited.add( (row-1, col) )
                        if row < y-1 and grid[row+1][col] == '1': visited.add( (row+1, col) )
                        if col > 0   and grid[row][col-1] == '1': visited.add( (row, col-1) )
                        if col < x-1 and grid[row][col+1] == '1': visited.add( (row, col+1) )

        return ans


        # ======================================================================== #


        #:  Solution (2) DFS
        #:  - time complexity: O(m*n)
        #:  - space complexity: O(m*n)
        def explore( i, j ):
            #:  turn the element to 0 to avoid exploring again
            grid[i][j] = '0'

            if i > 0   and grid[i-1][j] == '1': explore( i-1, j )
            if i < y-1 and grid[i+1][j] == '1': explore( i+1, j )
            if j > 0   and grid[i][j-1] == '1': explore( i, j-1 )
            if j < x-1 and grid[i][j+1] == '1': explore( i, j+1 )


        ans = 0
        for i in xrange( y ):
            for j in xrange( x ):
                if grid[i][j] == '1':
                    ans += 1
                    explore( i, j )

        return ans
