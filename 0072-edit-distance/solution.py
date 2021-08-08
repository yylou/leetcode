class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # (base case)
        if not word1 and not word2: return 0
        if not word1 or not word2: return len(word1) + len(word2)

        # ==================================================
        #  String + Dynamic Programming                    =
        # ==================================================
        # time  : O(mn)
        # space : O(mn)
        
        table = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1): table[i][0] = i
        for j in range(len(word2) + 1): table[0][j] = j
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]: table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        
        return table[-1][-1]