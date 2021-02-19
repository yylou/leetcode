class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        length = len( strs )

        ##  (edge case)  only one string
        if length == 1 : return [strs]

        ##  string sorting solution
        retHashTable = {}

        for string in strs :
            ##  the sorting returns the list, we need to JOIN them into a string to be the KEY of the hash table
            sortedString = ''.join( sorted(string) )

            if sortedString not in retHashTable : retHashTable[sortedString] = [string]
            else : retHashTable[sortedString].append( string )

        return retHashTable.values()
