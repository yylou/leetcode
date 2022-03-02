class Solution:
    def validPalindrome(self, s: str) -> bool:
        # (base case)
        if len(s) == 1 or len(s) == 2: return True

        # ==================================================
        #  Two Pointer                                     =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        return self._validPalindrome(s, True)

    def _validPalindrome(self, s: str, skip: bool) -> bool:
        # (base case)
        if len(s) == 1: return True

        l, r = 0, len(s) - 1
        while l < r:
            if   s[l] != s[r] and     skip: return self._validPalindrome(s[l+1:r+1], False) or self._validPalindrome(s[l:r], False)
            elif s[l] != s[r] and not skip: return False

            l, r = l+1, r-1

        return True
