class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        ##  Solution (2) Trie Tree Data Structure
        length = len( words )
        words.sort( key=len, reverse=True )

        retVal = []
        trie = Trie()

        for i in range( length ):
            ##  IGNORE checking the first and longest word, only do INSERT
            if i == 0:
                for j in range( len(words[i]) ):
                    trie.insert( words[i][j:] )
            else:
                ##  CHECK whether any substring == current word
                if trie.startswith( words[i] ):
                    retVal.append( words[i] )

                ##  INSERT into trie
                for j in range( len(words[i]) ):
                    trie.insert( words[i][j:] )

        return retVal

class Trie:
    def __init__( self ):
        self.root = {}

    def insert( self, string ):
        curNode = self.root

        for char in string:
            ##  not exist, CREATE node
            if not curNode.get( char ): curNode[char] = {}

            ##  PURPOSE: for TRAVESAL to print each substring (instead of printing POSTFIX only)
            curNode['#'] = ''

            curNode = curNode[char]

        curNode['end'] = True

    def search( self, word ):
        curNode = self.root

        for char in word:
            node = curNode.get( char )

            if not node:
                return False

            curNode = node

        return True if 'end' in curNode else False

    def startswith( self, word ):
        curNode = self.root

        for char in word:
            node = curNode.get( char )

            if not node:
                return False

            curNode = node

        return True

    ##  BACK tracking by recursion
    def travesal( self, node=None ):
        if node == None:
            node = self.root

        retVal = []

        for key, value in node.items():
            if key != 'end' and key != '#':
                for element in self.travesal( value ):
                    retVal.append( key + element )
            else:
                retVal.append( '' )

        return retVal
