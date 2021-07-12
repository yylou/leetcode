class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # (base case)
        if not s: return 0
        
        # ==================================================
        #  Hash Table + Sliding Window (Two Pointer)       =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        table = set()
        slowP, fastP = 0, 0
        ans = float('-inf')
        
        while fastP < len(s):
            if s[fastP] not in table:
                table.add(s[fastP])
                fastP += 1
                ans = max(ans, fastP - slowP)
                
            else:
                table.remove(s[slowP])
                slowP += 1
                
        return ans
