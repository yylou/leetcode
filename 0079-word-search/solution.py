class Solution:    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # ==================================================
        #  Array + DFS + Backtracking                      =
        # ==================================================
        # time  : O(m*3^k), m is the number of starting positions, k is the length of word
        # space : O(m+x*y+2k)
        
        self.board, self.word = board, word
        self.x, self.y, self.k = len(board[0]), len(board), len(word)
        
        starting, tableB, tableW = set(), dict(), dict()
        
        #  (candidate position & char existence table) x*y iterations
        for i in range(self.y):
            for j in range(self.x):
                if board[i][j] == word[0]: starting.add((i, j))
                tableB[board[i][j]] = tableB.get(board[i][j], 1)
                
        #  (check word for char existence record) k iterations
        for char in word:
            tableW[char] = tableW.get(char, 1)
            
            if char not in tableB: return False
            if tableW[char] > tableB[char]: return False
        
        #  (DFS)
        for i, j in starting:
            if self.DFS(0, j, i): return True
            
        return False
    
    def DFS(self, index, x, y) -> bool:
        if index == self.k - 1: return True
        
        nextChar = self.word[index+1]
        
        if y - 1 >= 0 and self.board[y-1][x] == nextChar:
            self.board[y][x] = '.'
            if self.DFS(index + 1, x, y - 1): return True
            self.board[y][x] = self.word[index]
            
        if y + 1 < self.y and self.board[y+1][x] == nextChar:
            self.board[y][x] = '.'
            if self.DFS(index + 1, x, y + 1): return True
            self.board[y][x] = self.word[index]
            
        if x - 1 >= 0 and self.board[y][x-1] == nextChar:
            self.board[y][x] = '.'
            if self.DFS(index + 1, x - 1, y): return True
            self.board[y][x] = self.word[index]
            
        if x + 1 < self.x and self.board[y][x+1] == nextChar:
            self.board[y][x] = '.'
            if self.DFS(index + 1, x + 1, y): return True
            self.board[y][x] = self.word[index]
            
        return False
