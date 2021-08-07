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
        
    '''
    def longestPalindrome(self, s: str) -> str:
        # (base case)
        if len(s) < 2: return s

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
    '''