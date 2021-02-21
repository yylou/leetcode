class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        length_h = len( haystack )
        length_n = len( needle )

        ##  (edge case)
        #   (1) needle is empty --> 0
        #   (2) haystack is empty --> -1
        #   (3) length of needle > length of haystack --> -1
        if not needle : return 0
        if not haystack : return -1
        if length_n > length_h : return -1

        ##  no need to loop through the input string
        ##  only need to check for the string in 'len(haystack) - len(needle)' index
        for i in range( length_h - length_n + 1 ) :
            if haystack[i:i+length_n] == needle : return i

        return -1
