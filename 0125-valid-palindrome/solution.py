class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        n = len(s)

        ##  (edge case) s only has one char
        if n == 1: return True

        s = s.lower()

        ##  Solution (1) two-pointer
        left, right = 0, n-1
        while left < right:
            while left < right and not s[left].isalnum(): left += 1
            while left < right and not s[right].isalnum(): right -= 1

            if s[left] != s[right]: return False

            left += 1
            right -=1

        return True
