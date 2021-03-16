class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ##  (edge case) length of 'nums' == 1
        if len(nums) == 1: return [nums]

        def recursive( curStr, candidate ):
            ##  END of recursion
            if not candidate:
                self.retVal.append( curStr )

            ##  ITERATE for each possible combination by ROTATING candidate (list of integers)
            else:
                for i in xrange( len(candidate) ):
                    num = candidate.pop(0)
                    recursive( curStr + [num], candidate[:] )
                    candidate.append( num )

        self.retVal = []
        recursive( [], nums )
        return self.retVal
