class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ##  (1) sorting solution
        # return True if sorted(s) == sorted(t) else False


        ##  (2) hash table solution
        hash_table = {}

        ##  record the existence of each char
        for char in s :
            if char not in hash_table : hash_table[char] = 1
            else : hash_table[char] += 1

        for char in t :
            ##  out of the record --> FALSE
            if char not in hash_table : return False
            else :
                hash_table[char] -= 1

                ##  the existence is more than the record --> FALSE
                if hash_table[char] < 0 : return False

        ##  for any remaining char --> FALSE
        for key, value in hash_table.items() :
            if value != 0 : return False

        return True
