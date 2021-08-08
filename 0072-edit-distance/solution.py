class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #  (base case)
        if not word1 and not word2: return 0
        if not word1 or not word2: return len(word1) + len(word2)

        # ==================================================
        #  String + Dynamic Programming                    =
        # ==================================================
        # time  : O(m*n)
        # space : O(m*n)
        
        self.word1, self.word2 = word1, word2
        self.n1, self.n2 = len(word1), len(word2)
        
        self.table = [[-1 for _ in range(self.n2)] for _ in range(self.n1)]
        
        return self.dp(0, 0)
        
    def dp(self, index1, index2) -> int:
        #  if one of string reaches the end, return the remaining length of the other string
        if index1 == self.n1: return self.n2 - index2
        if index2 == self.n2: return self.n1 - index1
        
        if self.table[index1][index2] != -1: return self.table[index1][index2]
        
        #  (SKIP) move both indexes without increasing moves
        if self.word1[index1] == self.word2[index2]: 
            self.table[index1][index2] = self.dp(index1 + 1, index2 + 1)
            
        else:
            insert  = 1 + self.dp(index1,     index2 + 1)
            delete  = 1 + self.dp(index1 + 1, index2)
            replace = 1 + self.dp(index1 + 1, index2 + 1)
            
            self.table[index1][index2] = min(insert, delete, replace)
            
        return self.table[index1][index2]