class Solution:
    def reverseWords(self, s: str) -> str:
        
        # ==================================================
        #  String                                          =
        # ==================================================
        # time  : O(n), n is the length of s
        # space : O(m), m is the number of words in s
        
        l, r = 0, len(s) - 1
        while s[l] == ' ': l += 1
        while s[r] == ' ': r -= 1
            
        words, word = [], ''
        while l <= r:
            if s[l] == ' ':
                if word: words.append(word)
                word = ''
                l += 1
                continue
                
            word += s[l]
            l += 1
        
        if word: words.append(word)
        
        ans = ''
        for i in range(len(words)-1, -1, -1):
            ans += words[i] + ' '
            
        return ans[:-1]
    
    '''
    def reverseWords(self, s: str) -> str:
        return ' '.join( reversed( s.split() ) )
    '''