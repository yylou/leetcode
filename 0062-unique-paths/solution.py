class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        #:  (edge case) m == n == 1
        if m == n == 1: return 1

        pathRecord = [[1] + [0 for i in xrange(n-1)] for j in xrange(m)]
        pathRecord[0] = [1] * n

        for i in xrange( 1, m ):
            for j in xrange( 1, n ):
                pathRecord[i][j] = pathRecord[i-1][j] + pathRecord[i][j-1]

        return pathRecord[m-1][n-1]
