# Problem
[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # (base case)
        if len(s) < 2: return s
        
        # ==================================================
        #  Expand around Corner                            =
        # ==================================================
        # time  : O(n^2)
        # space : O(1)
        
        self.ret = ''
        self.maxLen = 0
        
        for i in range(len(s)):
            # ODD length (aabbdde -> [a'a'b]bdde, a[a'b'd], ..., aabb[d'd'e])
            self.expand(s, i, i)

            # EVEN length (aabbdde -> [a'a']bbdde, a[a'b']bdde, ..., aabbd[d'e'])
            self.expand(s, i, i + 1)
            
        return self.ret
    
    def expand(self, s: str, l: int, r: int) -> None:
        while l >=0 and r < len(s) and s[l] == s[r]:
            if(r - l + 1) > self.maxLen:
                self.ret = s[l:r+1]
                self.maxLen = len(self.ret)
            l -= 1
            r += 1
```

```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # (base case)
        if not s or len(s) == 1: return s
    
        # ==================================================
        #  Dynamic Programming                             =
        # ==================================================
        # time  : O(n^2)
        # space : O(n^2)
        
        ret = ''
        
        # dp[i][j] = True == s[i:j] = Palindrome
        dp = [[None] * len(s) for i in range(len(s))]
        
        for i in range(len(s)):
            for j in range(i+1):
                if i == j: dp[i][j] = True
                elif i == j+1: dp[i][j] = s[i] == s[j]
                else: dp[i][j] = (dp[i-1][j+1] and s[i] == s[j])
                
                if dp[i][j] and i - j + 1 > len(ret): ret = s[j:i+1]
                    
        return ret
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n^2)
     * @space : O(1)
     */

    private int start, end, maxLen;

    public String longestPalindrome(String s) {
        int len = s.length();
        
        if(len < 2) return s;

        for(int i=0 ; i<len-1 ; i++) {
            extendPalindrome(s, i, i);      // odd  length
            extendPalindrome(s, i, i+1);    // even length
        }
        
        return s.substring(start, end + 1);
    }

    private void extendPalindrome(String s, int j, int k) {
        while(j >= 0 && k < s.length() && s.charAt(j) == s.charAt(k)) {
            j--;
            k++;
        }
        
        if(k - j - 1 > maxLen) {
            start = j + 1;
            end = k - 1;
            maxLen = k - j - 1;
        }
    }
}
```
