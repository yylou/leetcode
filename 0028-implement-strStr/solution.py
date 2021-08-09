class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # (base case)
        if not needle: return 0
        if not haystack: return -1
        if len(needle) > len(haystack): return -1
        
        # ==================================================
        #  String + Two Pointer                            =
        # ==================================================
        # n = length of haystack
        # m = length of needls
        # time  : O(nm)
        # space : O(1)
        
        start, end = 0, len(needle)
        
        while end-1 < len(haystack):
            if haystack[start:end] == needle: return start
            else:
                start += 1
                end   += 1
            
        return -1
    
        '''
        # ==================================================
        #  KMP Pattern Matching (Substring search)         =
        # ==================================================
        # n = length of haystack
        # m = length of needls
        # time  : O(n+m)
        # space : O(m)
        #
        # https://github.com/yylou/leetcode-problem-solving/blob/main/0028-implement-strStr/solution-KMP.py
        '''
        
        '''
        # ==================================================
        #  Python built-in Function                        =
        # ==================================================
        try:
            return haystack.index( needle )
        except:
            return -1
        '''