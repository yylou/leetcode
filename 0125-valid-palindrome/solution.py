class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  (base case)
        if len(s) == 1: return True
        
        # ==================================================
        #  String + Two Pointer                            =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        left, right = 0, len(s) - 1
         
        while left < right:
            while left  < len(s) and not s[left].isalnum(): left += 1
            while right >= 0     and not s[right].isalnum(): right -= 1
                
            if left > right or s[left].lower() != s[right].lower(): return True
            
            left  += 1
            right -= 1
            
        return True
    
'''
Java Solution
==================================================================================================
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
==================================================================================================
'''
