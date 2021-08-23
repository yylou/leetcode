class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
     
    public boolean isPalindrome(int x) {
        if(x < 0 || (x != 0 && x % 10 == 0)) return false;
        if(x < 10) return true;
        
        int rev = 0;
        
        while(x > rev) {
            rev = rev*10 + x % 10;;
            x /= 10;
        }
        
        if(x == rev || x == rev/10) return true;
        else return false;
    }
}