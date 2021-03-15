class Solution(object):
    def expand(self, string, length, start, end):
        left = start
        right = end

        ##  keep EXPANDING
        while left >= 0 and right < length and string[left] == string[right]:
            left -= 1
            right += 1

        ##  LEFT needs to be added '1', RIGHT does not need (due to string[LEFT:RIGTH])
        return left+1, right, right-left-1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ##  (edge case) length of 's' == 1
        length = len(s)
        if not s or length == 1: return s

        ##  Solution (1) Find palindrome string with ODD length at first, then check for EVEN length
        ##  - time complexity: O(n)
        retStr = ''
        expand = 0

        ##  ODD length (aabbdde -> [a'a'b]bdde, a[a'b'd], ..., aabb[d'd'e])
        for i in xrange( length ):
            while i-expand >= 0 and i+expand < length and s[i-expand:i] == s[i+expand:i:-1]:
                retStr = s[i-expand:i+expand+1]
                expand += 1

        ##  EVEN length (aabbdde -> [a'a']bbdde, a[a'b']bdde, ..., aabbd[d'e'])
        for i in xrange( 1, length ):
            while i-expand >= 0 and i+expand <= length and s[i-expand:i] == s[i+expand-1:i-1:-1]:
                retStr = s[i-expand:i+expand]
                expand += 1

        return retStr


        # ============================================================================================= #


        ##  Solution (2) Iterate through string and EXPAND for both ODD and EVEN legnth each iteration
        ##  - time complexity: O(n^2)
        start, end, maxLen = 0, 0, float( 'inf' )*-1

        for i in xrange( length ):
            ##  ODD length of palindromic string
            s1, e1, len1 = self.expand( s, length, i, i )
            ##  EVEN length of palindromic string
            s2, e2, len2 = self.expand( s, length, i, i+1 )

            if len1 > len2 and len1 > maxLen: start, end, maxLen = s1, e1, len1
            elif len2 > len1 and len2 > maxLen: start, end, maxLen = s2, e2, len2

        return s[start:end]
