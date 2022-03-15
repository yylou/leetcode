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
            # ODD  length (aabbdde -> ['a']abbdde, a['a']bbdde, ..., aabbdd['e'])
            length, string = self.expand(s, i, i)
            if length >= maxLen: maxLen, maxStr = length, string
                
            # EVEN length (aabbdde -> ['a'a]bbdde, a['a'b]bdde, ..., aabbd['d'e])
            length, string = self.expand(s, i, i+1)
            if length >= maxLen: maxLen, maxStr = length, string
        
        return maxStr
        
    def expand(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l, r = l-1, r+1
            
        return r - l + 1, s[l+1:r]
        
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