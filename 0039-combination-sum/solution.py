class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        answer = []


        def recursive( target, tmpAnswer, index ):
            ##  FIT
            if target == 0:
                answer.append( tmpAnswer )
                return

            ##  SMALLER
            if target < candidates[index]:
                return

            for i in xrange( index, len(candidates) ):
                recursive( target - candidates[i], tmpAnswer + [candidates[i]], i )


        recursive( target, [], 0 )

        return answer
