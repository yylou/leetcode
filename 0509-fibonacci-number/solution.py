class Solution:
    def fib(self, n: int) -> int:
        #: (base case)
        if n == 0 or n == 1: return n
        
        # ==================================================
        #  Dynamic Programming                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        first, second = 0, 1
        
        for i in range( n - 1 ):
            tmp = first
            first = second
            second += tmp
            
        return second
    
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int fib(int n) {
        if( n == 0 || n == 1 ) return n;
        
        int first = 0, second = 1;
        
        for( int i=0 ; i<n-1 ; i++ ){
            int tmp = first;
            first = second;
            second += tmp;
        }
        
        return second;
    }
}
==================================================================================================
'''
