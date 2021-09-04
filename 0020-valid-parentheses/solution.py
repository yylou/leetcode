class Solution:
    def isValid(self, s: str) -> bool:
        # (base case)
        if len(s) == 1: return False
        
        # ==================================================
        #  String + Stack                                  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        table = { 
            ')': '(', 
            ']': '[', 
            '}': '{' 
        }
        stack = []
        
        if s[0] in table: return False
        
        for char in s:
            if char in table:
                # if stack is alread empty, return False
                if not stack: return False 
                
                item = stack.pop()
                
                if item != table[char]: return False
                
            else:
                stack.append( char )
                
        # check stack's capacity before returning True
        return not stack