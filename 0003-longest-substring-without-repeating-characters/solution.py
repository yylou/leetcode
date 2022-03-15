class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # ==================================================
        #  Hash Table + Sliding Window (Two Pointer)       =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        # (base case)
        if not s: return 0
        if len(s) == 1: return 1
        
        curStr = set()
        maxLen = float('-inf')
        l, r = 0, 0
        
        while r < len(s):
            # (1) No duplicate, add to table and move fast pointer
            if s[r] not in curStr: 
                curStr.add(s[r])
                maxLen = max(maxLen, len(curStr))
                r += 1
            
            # (2) Duplicate, remove from table and move slow pointer
            else:
                curStr.remove(s[l])
                l += 1
            
        return maxLen