class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #  (base case)
        if m == 1 or n == 1: return 1
        
        # ==================================================
        #  Array + Dynamic Programming                     =
        # ==================================================
        # time  : O(m*n)
        # space : O(m*n)
        
        table = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i-1][j] + table[i][j-1]
                
        return table[-1][-1]
    
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(m*n)
     * @space : O(m*n)
     */
     
    public int uniquePaths(int m, int n) {
        /* base case */
        if(m == 1 || n == 1) return 1;
        
        int[][] table = new int[m][n];
        for(int i=0 ; i<m ; i++) Arrays.fill(table[i], 1);
        
        for(int i=1 ; i<m ; i++) {
            for(int j=1 ; j<n ; j++) {
                table[i][j] = table[i-1][j] + table[i][j-1];
            }
        }
        
        return table[m-1][n-1];
    }
}
==================================================================================================
'''
