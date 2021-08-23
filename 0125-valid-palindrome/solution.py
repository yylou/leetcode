class Solution:
    def isPalindrome(self, s: str) -> bool:
        # (base case)
        if len(s) == 1: return True
        
        # ==================================================
        #  String + Two Pointer                            =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        left, right = 0, len(s) - 1
         
        while left < right:
            # consider only alphanumeric characters
            while left  < len(s) and not s[left].isalnum(): left += 1
            while right >= 0     and not s[right].isalnum(): right -= 1
                
            if left > right: return True
            
            # ignoring cases
            if s[left].lower() != s[right].lower(): return False
            
            left  += 1
            right -= 1
            
        return True