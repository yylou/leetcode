##  Sliding Window solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, i, j = 0, 0, 0
        length = len( s )
        hash_table = {}

        ##  edge case handling: s = ""
        if length == 0 : return 0

        while i < length and j < length :
            ##  meeting new char, add into hash table and renew the longest length, then move the fast-runner pointer
            if s[j] not in hash_table :
                hash_table[s[j]] = j
                j += 1
                ans = max( ans, j-i )

            ##  meeting existing char, removing from hash table and move the slow-runner pointer
            else :
                del hash_table[s[i]]
                i += 1

        return ans
