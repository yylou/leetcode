class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
     
    public boolean isPalindrome(String s) {
        /* base case */
        if(s.length() == 1) return true;
        
        int left = 0, right = s.length() - 1;
        
        while(left < right) {
            while(left < s.length() && !Character.isLetterOrDigit(s.charAt(left))) left++;
            while(right >= 0 && !Character.isLetterOrDigit(s.charAt(right))) right--;
            
            if(left > right) return true;
            if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) return false;
            
            left++;
            right--;
        }
        
        return true;
    }
}