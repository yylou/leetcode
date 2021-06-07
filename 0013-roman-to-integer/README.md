# Problem
[13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

# Performance
![result](./result.png)

# Python
```Python
class Solution:
    def romanToInt(self, s: str) -> int:
        RtoI = {
            "I":  1,
            "IV": 4,
            "V":  5,
            "IX": 9,
            "X":  10,
            "XL": 40, 
            "L":  50,
            "XC": 90,
            "C":  100,
            "CD": 400,
            "D":  500,
            "CM": 900,
            "M":  1000,
        }
        
        # ==================================================
        #  String + Math (Left to Right)                   =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        ans   = 0
        index = 0
        
        while index < len(s):
            if index+1 < len(s) and s[index:index+2] in RtoI:
                ans += RtoI[s[index:index+2]]
                index += 2
            
            else:
                ans += RtoI[s[index]]
                index += 1
                
        return ans
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    public int romanToInt(String s) {
        
    }
}
```
