class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
    
    public boolean isPerfectSquare(int num) {
        /* base case */
        if(num == 1) return true;
        
        long l = 1, r = num;
        while(l < r) {
            long mid = l + (r - l) / 2;
            long val = mid * mid;
            
            if(val == num) return true;
            else if(val > num) r = mid;
            else if(val < num) l = mid + 1;
        }
        
        return false;
    }
}