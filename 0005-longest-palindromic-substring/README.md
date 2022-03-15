# Problem
[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

# Performance
![result-python](./result.png)
![result-java](./result-java.png)

# Python
```Python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # ==================================================
        #  Expand around Corner                            =
        # ==================================================
        # time  : O(n^2)
        # space : O(1)
        
        # (base case)
        if not s or len(s) == 1: return s
        
        maxLen, maxStr = 0, ''
        for i in range(len(s) - 1):
            length, string = self.expand(s, i, i)
            if length >= maxLen: maxLen, maxStr = length, string
                
            length, string = self.expand(s, i, i+1)
            if length >= maxLen: maxLen, maxStr = length, string
        
        return maxStr
        
    def expand(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l, r = l-1, r+1
            
        return r - l + 1, s[l+1:r]
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
