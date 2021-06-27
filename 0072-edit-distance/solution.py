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
            insert  = 1 + self.dp(index1    , index2 + 1)
            delete  = 1 + self.dp(index1 + 1, index2)
            replace = 1 + self.dp(index1 + 1, index2 + 1)
            
            self.table[index1][index2] = min(insert, delete, replace)
            
        return self.table[index1][index2]
    
'''
Java Solution
==================================================================================================
class Solution {
    /**  
     * @time  : O(m*n)
     * @space : O(m*n)
     */
     
    String word1, word2;
    int n1, n2;
    int[][] table;
    
    public int minDistance(String word1, String word2) {
        /* base case */
        if(word1 == null && word2 == null) return 0;
        if(word1 == null || word2 == null) return word1.length() + word2.length();
        
        this.word1 = word1;
        this.word2 = word2;
        this.n1 = word1.length();
        this.n2 = word2.length();
            
        this.table = new int[word1.length()][word2.length()];
        for(int i=0 ; i<word1.length() ; i++) {
            Arrays.fill(this.table[i], -1);
        }
        
        return dp(0, 0);
    }
    
    public int dp(int index1, int index2) {
        if(index1 == this.n1) return this.n2 - index2;
        if(index2 == this.n2) return this.n1 - index1;
        
        if(this.table[index1][index2] != -1) return this.table[index1][index2];
        
        if(this.word1.charAt(index1) == this.word2.charAt(index2)) {
            this.table[index1][index2] = dp(index1 + 1, index2 + 1);
            
        } else {
            int insert  = 1 + dp(index1,     index2 + 1);
            int delete  = 1 + dp(index1 + 1, index2);
            int replace = 1 + dp(index1 + 1, index2 + 1);
            
            this.table[index1][index2] = Math.min(Math.min(insert, delete), replace);
        }
        
        return this.table[index1][index2];
    }
}   
==================================================================================================
'''
