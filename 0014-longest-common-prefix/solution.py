##  Trie solution, related to LeetCode problem - 208. Implement Trie (Prefix Tree)
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curNode = self.root

        for char in word:
            ##  check the existence of CHAR, if not found, create a new hash_table to record CHAR
            if char not in curNode: curNode[char] = dict()

            curNode = curNode[char]

        curNode['end_of_word'] = True


    def longestCommonPrefix(self):
        ret_value = ''
        curNode = self.root

        while True:
            if len( curNode ) == 1 and 'end_of_word' not in curNode : ret_value += curNode.keys()[0]
            else : return ret_value

            curNode = curNode[curNode.keys()[0]]

        return ret_value


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        length = len( strs )

        ##  edge case handling
        if not strs : return ''
        if strs[0] == '' : return ''
        if length == 1 : return strs[0]

        trie_data = Trie()

        ##  insert each string into Trie data structure
        for i in range( length ) : trie_data.insert( strs[i] )

        return trie_data.longestCommonPrefix()
