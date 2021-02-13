##  instead of initializing a new data structure as Trie's node, using hash_table only
class Trie(object):

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

        ##  add one entry, 'end_of_word', to flag the status of reaching the end of word
        curNode['end_of_word'] = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root

        for char in word:
            ##  certain CHAR does not exist, return FALSE
            if char not in curNode: return False

            curNode = curNode[char]

        ##  if the end CHAR of word is found, need to check whether it is a complete word or just substring
        return True if 'end_of_word' in curNode else False


    ##  same as SEARCH operation, except no need to check the key 'end_of_word'
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root

        for char in prefix:
            ##  certain CHAR does not exist, return FALSE
            if char not in curNode: return False

            curNode = curNode[char]

        return True



##  Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
