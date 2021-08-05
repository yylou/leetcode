class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public void reverseString(char[] s) {
        /* base case */
        if(s.length == 1) return;
        
        int l = 0, r = s.length - 1;
        while(l <= r) {
            char tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;
                
            l++;
            r--;
        }
    }
}