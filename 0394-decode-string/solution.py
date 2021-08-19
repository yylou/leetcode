class Solution:
    def decodeString(self, s: str) -> str:
        
        # ==================================================
        #  String + Stack                                  =
        # ==================================================
        # time  : O(n)
        # space : O(m), m is the number of pairs of square brackets
        
        ans, stack, curNum = '', [], 0
        
        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)
                
            elif char == '[':
                stack.append((ans, curNum))
                ans, curNum = '', 0
                
            elif char == ']':
                prev, num = stack.pop()
                ans = prev + num * ans
                
            else:
                ans += char
        
        return ans