class Solution {
    /**
     * @time  : O(nm)
     * @space : O(1)
     */

    public int strStr(String haystack, String needle) {
        /* base case */
        if(needle.length() == 0) return 0;
        if(haystack.length() == 0 || needle.length() > haystack.length()) return -1;
        
        for(int i=0; i<(haystack.length()-needle.length()+1);i++) {
            if (haystack.substring(i,i+needle.length()).equals(needle)) return i;
        }
        return -1;
    }
}