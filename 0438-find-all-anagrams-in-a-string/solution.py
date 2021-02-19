class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        ##  (3) sliding window solution: record the existence of the first n char, then sliding towards to the end
        lengthS = len(s)
        lengthP = len(p)

        ##  (edge case handling) lengthP > lengthS
        if lengthP > lengthS : return []

        retValue = []

        ##  loop through each char in 'p' string and record the existence in the hash table
        targetHashTable = {}
        for char in p :
            if char not in targetHashTable : targetHashTable[char] = 1
            else : targetHashTable[char] += 1

        ##  BASE case for sliding window implementation: s[:legnthOfPstring]
        curHashTable = {}
        for char in s[:lengthP] :
            if char not in curHashTable : curHashTable[char] = 1
            else : curHashTable[char] += 1

        if targetHashTable == curHashTable : retValue.append( 0 )

        counter = 0
        for char in s[lengthP:] :
            if char not in curHashTable : curHashTable[char] = 1
            else : curHashTable[char] += 1

            ##  if the no longer exist, delete the key to prevent wrong comparison
            curHashTable[s[counter]] -= 1
            if curHashTable[s[counter]] == 0 : del curHashTable[s[counter]]

            if targetHashTable == curHashTable : retValue.append( counter+1 )

            counter += 1

        return retValue

        # =============================================================================== #

        ##  (1) sorting solution --> Time Limit Exceeded
        sortedP = sorted(p)

        lengthS = len(s)
        lengthP = len(p)

        ret_value = []

        for i in range( lengthS - lengthP + 1 ) :
            if sorted(s[i:i+lengthP]) == sortedP : ret_value.append( i )

        return ret_value

        # =============================================================================== #

        ##  (2) hash table solution --> Time Limit Exceeded
        lengthS = len(s)
        lengthP = len(p)

        ret_value = []

        hashTableP= {}
        for char in p :
            if char not in hashTableP : hashTableP[char] = 1
            else : hashTableP[char] += 1

        for i in range( lengthS - lengthP + 1 ) :
            tmpHashTable = {}
            for char in s[i:i+lengthP] :
                if char not in tmpHashTable : tmpHashTable[char] = 1
                else : tmpHashTable[char] += 1

            if tmpHashTable == hashTableP : ret_value.append( i )

        return ret_value
