class Solution {
    /**
     * @time  : O(n^2)
     * @space : O(1)
     */

    private int start, end, maxLen;

    public String longestPalindrome(String s) {
        int len = s.length();
        
        if(len < 2) return s;

        for(int i=0 ; i<len-1 ; i++) {
            extendPalindrome(s, i, i);      // odd  length
            extendPalindrome(s, i, i+1);    // even length
        }
        
        return s.substring(start, end + 1);
    }

    private void extendPalindrome(String s, int j, int k) {
        while(j >= 0 && k < s.length() && s.charAt(j) == s.charAt(k)) {
            j--;
            k++;
        }
        
        if(k - j - 1 > maxLen) {
            start = j + 1;
            end = k - 1;
            maxLen = k - j - 1;
        }
    }
}