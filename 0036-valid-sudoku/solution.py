class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowHashTable = { 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {} }
        colHashTable = { 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {} }
        squHashTable = { 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {} }

        for i in range( len(board) ):
            row = board[i]

            for j in range( len(row) ):
                if row[j] == '.': continue

                ##  ROW
                if row[j] in rowHashTable[i]: return False
                rowHashTable[i][row[j]] = 1

                ##  COL
                if row[j] in colHashTable[j]: return False
                colHashTable[j][row[j]] = 1

                ##  SQU
                squID = i//3*3 + j//3
                if row[j] in squHashTable[squID]: return False
                squHashTable[squID][row[j]] = 1

        return True
