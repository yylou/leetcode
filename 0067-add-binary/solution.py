class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # ==================================================
        #  String + Math                                   =
        # ==================================================
        # time  : O(max(n,m))
        # space : O(1)
        
        ans = ''
        n1, n2, carry = len(a) - 1, len(b) - 1, 0
        
        while n1 >= 0 or n2 >= 0:
            bit1 = int(a[n1]) if n1 >= 0 else 0
            bit2 = int(b[n2]) if n2 >= 0 else 0
            
            result = bit1 + bit2 + carry
            if result > 1:
                result -= 2
                carry = 1
            else:
                carry = 0
                
            ans = str(result) + ans
            
            n1 -= 1
            n2 -= 1
            
        if carry: ans = '1' + ans
        return ans