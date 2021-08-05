class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # ==================================================
        #  String                                          =
        # ==================================================
        # time  : O(M), M is the total number of chars in words
        # space : O(1)
        
        table = dict()
        for i in range(len(order)): table[order[i]] =  i
            
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # (current string's length > adjacent string's length)
                if j+1 > len(words[i+1]): return False
                
                if words[i][j] != words[i+1][j]:
                    if table[words[i][j]] > table[words[i+1][j]]: return False
                    break
                    
        return True