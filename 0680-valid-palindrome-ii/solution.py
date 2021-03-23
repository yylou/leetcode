class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ##  (edge case) length == 1 or 2
        n = len(s)
        if n == 1 or n == 2: return True


        ##  Solution (1) check by reversing string
        left, right = 0, n-1
        while left <= right:
            if s[left] != s[right]:
                ##  skip one char in left side and right side, then reverse string to check
                if s[left+1:right+1] == s[left+1:right+1][::-1]: return True
                if s[left:right] == s[left:right][::-1]: return True

                return False

            else:
                left  += 1
                right -= 1

        return True


        # ========================================================================================= #


        ##  Solution (2) check by two check process branches
        def check( s, skip ):
            left, right = 0, len(s)-1

            while left <= right:
                if s[left] != s[right]:
                    if skip:
                        if check( s[left+1:right+1], False ) or check( s[left:right], False ):
                            return True
                        else:
                            return False
                    else:
                        return False

                else:
                    left  += 1
                    right -= 1

            return True

        return check( s, True )
