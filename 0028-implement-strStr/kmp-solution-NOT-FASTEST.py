class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        ##  KMP solution: compute LPS --> repeat pattern record
        def lps( string, length ) :
            jumpCounter, moveCounter = 0, 1
            lps = [0] + [-1] * ( length-1 )
            while moveCounter < length :
                if string[jumpCounter] == string[moveCounter] :
                    lps[moveCounter] = jumpCounter+1
                    jumpCounter += 1
                    moveCounter += 1
                else :
                    ## JUMP --> to the index of previously same substring
                    if jumpCounter != 0 :
                        jumpCounter = lps[jumpCounter-1]

                    ## CANNOT JUMP --> move forward
                    else :
                        lps[moveCounter] = 0
                        moveCounter += 1

            return lps

        lengthH = len( haystack )
        lengthN = len( needle )

        ##  (edge case)
        #   (1) needle is empty --> 0
        #   (2) haystack is empty --> -1
        #   (3) length of needle > length of haystack --> -1
        if not needle : return 0
        if not haystack : return -1
        if lengthN > lengthH : return -1

        arrayLPS = lps( needle, lengthN )

        ##  KMP algorithm
        jumpCounter, moveCounter = 0, 0
        while moveCounter < lengthH :
            if haystack[moveCounter] == needle[jumpCounter] :
                jumpCounter += 1
                moveCounter += 1
            else :
                ## JUMP --> to the index of the previously same substring, instead of starting from the begining
                if jumpCounter != 0 :
                    jumpCounter = arrayLPS[jumpCounter-1]

                ## CANNOT JUMP --> move forward
                else :
                    moveCounter += 1

            if jumpCounter == lengthN : return moveCounter - lengthN

        return -1
