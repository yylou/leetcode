class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len( A )

        ##  (edge case) arr is empty
        if length == 0: return 0
        ##  (edge case) arr only has one element
        if length == 1: return 0
        ##  (edge case) arr only has two elements
        if length == 2:
            if A[0] == A[1]: return 1
            else: return 0

        ##  SORT: increase from the SMALLEST number
        A.sort()

        moves = 0
        prevNum = A[0] - 1

        for num in A:
            print prevNum

            ##  unique, move forward
            if num > prevNum:
                prevNum = num

            ##  DUPLICATE (num <= prevNum)
            else:
                ##  to be unique, need to INCREASE multiple
                ##  = make the number be bigger than previous number for '1'
                ##  ex. [1,4,4,4,6] -> [1,4,5,(4),6]
                ##  to make 4 need to be 5+1, need to increase 5-4+1 = 2
                moves += (prevNum - num) + 1

                prevNum += 1

        return moves
