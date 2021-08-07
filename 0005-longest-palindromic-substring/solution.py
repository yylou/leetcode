class Solution:
    def longestPalindrome(self, s: str) -> str:
        # (base case)
        if not s or len(s) == 1: return s
    
        # ==================================================
        #  Expand around Corner                            =
        # ==================================================
        # time  : O(n^2)
        # space : O(1)
        
        ret = ''
        maxLen = 0
        
        for i in range(len(s)):
            # ODD length (aabbdde -> [a'a'b]bdde, a[a'b'd], ..., aabb[d'd'e])
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    ret = s[l:r+1]
                    maxLen = len(ret)
                l -= 1
                r += 1
            
            # EVEN length (aabbdde -> ['aa']bbdde, a['ab']bdde, ..., aabbd['de'])
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    ret = s[l:r+1]
                    maxLen = len(ret)
                l -= 1
                r += 1
            
        return ret
        
        '''
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