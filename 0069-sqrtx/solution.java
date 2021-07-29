class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */

    public int mySqrt(int x) {
        if( x == 0 ) return 0;
        if( x  < 4 ) return 1;
        if( x == 4 ) return 2;
        
        int l = 1, r = x;
        
        while(l < r){
            int mid = l + (r - l) / 2;
            
            // use LONG since mid * mid can be larger than INT.MAX
            long num = (long) mid * mid;
            
            if(num == x) return mid;
            else if(num > x) r = mid;
            else if(num < x) l = mid + 1;
        }
        
        return l - 1;
    }
}