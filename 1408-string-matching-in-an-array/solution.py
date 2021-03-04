class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        ##  Solution (1) Iterative
        length = len( words )
        words.sort( key=len )

        retVal = []

        ##  IGNORE the last word (since the longest word does not work)
        for i in range( length-1 ):
            ##  LOOP through the remaining words
            for element in words[i+1:]:
                if words[i] in element:
                    retVal.append( words[i] )
                    break

        return retVal
