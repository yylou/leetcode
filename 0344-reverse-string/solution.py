class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        ##  non-recursive solution with two pointers in while loop
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
