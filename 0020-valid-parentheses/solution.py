class Solution:
    def isValid(self, s: str) -> bool:
        # (base case)fy
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
        
        # return False if first char is right-side parenthesis
        if s[0] in table: return False
        
        for char in s:
            if char in table:
                # return False if stack is already empty
                if not stack: return False 
                
                if stack.pop() != table[char]: return False
                
            else:
                stack.append( char )
                
        # check stack's capacity before returning True
        return not stack