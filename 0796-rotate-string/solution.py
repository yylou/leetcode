class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        ##  (edge case) compare two lengths
        if len(A) != len(B): return False

        A += A

        return True if B in A else False
