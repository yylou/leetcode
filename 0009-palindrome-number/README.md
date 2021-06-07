# Problem
[9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

# Performance
![result](./result.png)

# Python
```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #:  (negative / edge case)
        if x <  0 or (x != 0 and x % 10 == 0): return False
        if x < 10: return True
        
        # ==================================================
        #  Math                                            =
        # ==================================================
        # time  : O(log(n))
        # space : O(1)
        
        rev = 0
        
        #:  loop until reversed integer > divided integer
        #:  - ex: 12345, rev = 543, x = 12
        while x > rev:
            pop = x % 10
            x //= 10
            
            rev = rev*10 + pop
        
        #:  for length is odd, middle digit could be ignored by // 10
        if x == rev or x == rev // 10: return True
        else: return False
        
        
        '''
        
        # ==================================================
        #  String                                          =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        x = str(x)
        return x[::-1] == x
        
        '''
```

# Java
```Java
class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
    public boolean isPalindrome(int x) {
        if( x < 0 || (x != 0 && x % 10 == 0) ) return false;
        if( x < 10 ) return true;
        
        int rev = 0;
        
        while( x > rev ){
            rev = rev*10 + x % 10;;
            x /= 10;
        }
        
        if( x == rev || x == rev/10 ) return true;
        else return false;
    }
}
```
