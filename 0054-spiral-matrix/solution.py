class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        #:  (edge case)
        x = len(matrix[0])
        y = len(matrix)
        if y == 1: return matrix[0]


        #:  Solution (1) 2-poitner
        total = x*y
        counter = 0
        stack = []

        for i in xrange( y // 2 + y % 2 ):
            if len(stack) == total: return stack

            xP = yP = i

            #:  (1) visit X in clockwise order
            while xP < x-i:
                stack.append( matrix[yP][xP] )
                xP += 1

            if len(stack) == total: return stack
            yP += 1
            xP -= 1

            #:  (2) visit Y in clockwise order
            while yP < y-i:
                stack.append( matrix[yP][xP] )
                yP += 1

            if len(stack) == total: return stack
            xP -= 1
            yP -= 1

            #:  (3) visit X in anti-clockwise order
            while xP >= i:
                stack.append( matrix[yP][xP] )
                xP -= 1

            if len(stack) == total: return stack
            yP -= 1
            xP += 1

            #:  (4) visit Y in anti-clockwise order
            while yP > i:
                stack.append( matrix[yP][xP] )
                yP -= 1

            if len(stack) == total: return stack

        return stack


        # ============================================================== #


        #:  Solution (2) POP matrix and check empty before POP
        stack = []
        while True:
            if not matrix: return stack
            for element in matrix.pop(0):
                stack.append( element )

            for i in xrange( len(matrix) ):
                if not matrix[i]: return stack
                stack.append( matrix[i].pop() )

            if not matrix: return stack
            for element in matrix.pop()[::-1]:
                stack.append( element )

            for i in xrange( len(matrix)-1, -1, -1 ):
                if not matrix[i]: return stack
                stack.append( matrix[i].pop( 0 ) )

        return stack
