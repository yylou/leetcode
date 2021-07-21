# Problem
[415. Add Strings](https://leetcode.com/problems/add-strings/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python3
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
```

# Java
```Java
class Solution {
    /**
     * @time  : O(max(m,n))
     * @space : O(1)
     */
    
    public String addStrings(String num1, String num2) {
        int p1 = num1.length() - 1, p2 = num2.length() - 1, carry = 0;
        
        StringBuilder ans = new StringBuilder();
        
        while(p1 >= 0 || p2 >= 0 || carry > 0) {
            int val1 = (p1 >= 0) ? num1.charAt(p1--) - '0' : 0;
            int val2 = (p2 >= 0) ? num2.charAt(p2--) - '0' : 0;
            int val = val1 + val2 + carry;
            carry = val / 10;
            val = val % 10;
            
            ans.append(val);
        }
        
        return ans.reverse().toString();
    }
}
```