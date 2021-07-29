class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
    
    public boolean isPerfectSquare(int num) {
        /* base case */
        if(num == 1) return true;
        
        int l = 1, r = num;
        while(l < r) {
            int mid = l + (r - l) / 2;
            long val = (long) mid * mid;
            
            if(val == num) return true;
            else if(val > num) r = mid;
            else if(val < num) l = mid + 1;
        }
        
        return false;
    }
}