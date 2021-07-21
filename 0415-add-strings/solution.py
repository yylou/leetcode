class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # ==================================================
        #  String + Math                                   =
        # ==================================================
        # time  : O(max(m,n))
        # space : O(1)
        
        ans, carry = '', 0
        
        p1, p2 = len(num1) - 1, len(num2) - 1
        while(p1 >= 0 or p2 >= 0 or carry > 0):
            val1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            val2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            
            ans = str(val) + ans
            p1 -= 1
            p2 -= 1
            
        return ans