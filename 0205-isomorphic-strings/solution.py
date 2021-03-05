class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        lengthS = len(s)

        ##  (edge case)
        if lengthS == 1: return True

        ##  Solution (1) - Using char mapping table to compare the pattern
        mappingTable = {}

        for i in range( lengthS ):
            if s[i] not in mappingTable:
                if t[i] in mappingTable.values(): return False
                mappingTable[s[i]] = t[i]
            else:
                if mappingTable[s[i]] != t[i]: return False

        return True

        # ========================================================================================= #

        ##  Solution (2) - Using sorted occurrence table to compare the pattern
        occurrenceS, occurrenceT = {}, {}

        for i in range( lengthS ):
            if not occurrenceS.get( s[i] ): occurrenceS[s[i]] = [i]
            else: occurrenceS[s[i]].append( i )

            if not occurrenceT.get( t[i] ): occurrenceT[t[i]] = [i]
            else: occurrenceT[t[i]].append( i )

        return True if sorted( occurrenceS.values() ) == sorted( occurrenceT.values() ) else False
