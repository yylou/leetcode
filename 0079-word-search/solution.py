class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        x = len(board[0])
        y = len(board)

        ##  (edge case) follow the constraints
        n = len(word)
        if n > x*y : return False

        ##  iterate through matrix to record index
        firstPosition = set()
        posRecord = {}
        for i in xrange( y ):
            for j in xrange( x ):
                if board[i][j] == word[0]: firstPosition.add( (i, j) )
                posRecord[board[i][j]] = posRecord.get( board[i][j], 0 ) + 1

        ##  iterate through word to count char existence
        charCount = {}
        for char in word:
            charCount[char] = charCount.get( char, 0 ) + 1

            ##  check whether char occurrence qualifies
            if char not in posRecord: return False
            if charCount[char] > posRecord[char]: return False


        def recursive( wordIndex, curPos, visited ):
            if wordIndex == n: return True

            ##  UP
            if curPos[0]-1 >= 0 and board[curPos[0]-1][curPos[1]] == word[wordIndex] and (curPos[0]-1, curPos[1]) not in visited:
                visited.add( (curPos[0]-1, curPos[1]) )
                if recursive( wordIndex+1, (curPos[0]-1, curPos[1]), visited ): return True
                visited.remove( (curPos[0]-1, curPos[1]) )

            ##  DOWN
            if curPos[0]+1 < y and board[curPos[0]+1][curPos[1]] == word[wordIndex] and (curPos[0]+1, curPos[1]) not in visited:
                visited.add( (curPos[0]+1, curPos[1]) )
                if recursive( wordIndex+1, (curPos[0]+1, curPos[1]), visited ): return True
                visited.remove( (curPos[0]+1, curPos[1]) )

            ##  LEFT
            if curPos[1]-1 >= 0 and board[curPos[0]][curPos[1]-1] == word[wordIndex] and (curPos[0], curPos[1]-1) not in visited:
                visited.add( (curPos[0], curPos[1]-1) )
                if recursive( wordIndex+1, (curPos[0], curPos[1]-1), visited ): return True
                visited.remove( (curPos[0], curPos[1]-1) )

            ##  RIGHT
            if curPos[1]+1 < x and board[curPos[0]][curPos[1]+1] == word[wordIndex] and (curPos[0], curPos[1]+1) not in visited:
                visited.add( (curPos[0], curPos[1]+1) )
                if recursive( wordIndex+1, (curPos[0], curPos[1]+1), visited ): return True
                visited.remove( (curPos[0], curPos[1]+1) )

            return False


        for pos in firstPosition:
            tmpSet = set()
            tmpSet.add( pos )
            if recursive( 1, pos, tmpSet ): return True

        return False
