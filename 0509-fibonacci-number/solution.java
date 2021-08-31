class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int fib(int n) {
        /* base case */
        if(n == 0 || n == 1) return n;
        
        int first = 0, second = 1;
        
        for(int i=0 ; i<n-1 ; i++) {
            int tmp = first;
            first = second;
            second += tmp;
        }
        
        return second;
    }
}