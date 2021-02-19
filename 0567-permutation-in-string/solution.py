class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        length1 = len(s1)
        length2 = len(s2)

        ##  (edge case) length of s1 == 0 or 1
        if length1 == 0 : return False
        if length1 == 1 and s1 in s2 : return True

        ##  (edge case) length of s1 > length of s2
        if length1 > length2 : return False


        ##  (2) sliding window solution w/ hash table
        hashTable1, hashTable2 = {}, {}

        for i in range( length1 ) :
            if s1[i] not in hashTable1 : hashTable1[s1[i]] = 1
            else : hashTable1[s1[i]] += 1

            if s2[i] not in hashTable2 : hashTable2[s2[i]] = 1
            else : hashTable2[s2[i]] += 1

        ##  when the length of two strings is equal --> check the equality of hash table
        if length1 == length2 :
            if hashTable1 == hashTable2 : return True
            else : return False

        ##  sliding through the remain string of s2
        counter = 0
        for char in s2[length1:] :
            if char not in hashTable2 : hashTable2[char] = 1
            else : hashTable2[char] += 1

            hashTable2[s2[counter]] -= 1
            if hashTable2[s2[counter]] == 0 : del hashTable2[s2[counter]]

            if hashTable1 == hashTable2 : return True

            counter += 1

        return False


        # ===================================================================== #


        ##  (1) sliding window solution w/ sorting--> not the BEST one
        # sortedS1 = ''.join( sorted(s1) )
        #
        # for i in range( length2 - length1 + 1 ) :
        #     if ''.join( sorted(s2[i:i+length1]) ) == sortedS1 : return True

        return False
