class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
     
    public int reverse(int x) {
        if( x == 0 ) return x;
        
        int ans = 0;
        
        while( x != 0 ){
            int pop = x % 10;
            x /= 10;
            
            if( ans > Integer.MAX_VALUE/10 || ( ans == Integer.MAX_VALUE / 10 && pop >  7 ) ) return 0;
            if( ans < Integer.MIN_VALUE/10 || ( ans == Integer.MIN_VALUE / 10 && pop < -8 ) ) return 0;
            ans = ans*10 + pop;
        }
        
        return ans;
    }
}