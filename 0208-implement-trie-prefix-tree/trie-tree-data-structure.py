#-*- coding: utf-8 -*-

# Author  : Mike Lou
# Date    : 2021/03/04
# Version : 1.0
#       1.0  (2021'0304) - Trie build-up

class Trie:
    def __init__( self ):
        self.root = {}

    def insert( self, string ):
        curNode = self.root

        for char in string:
            ##  not exist, CREATE node
            if not curNode.get( char ): curNode[char] = {}

            curNode = curNode[char]

        curNode['end'] = True

    ##  need to check whether END (key) exists before return
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
            if key != 'end':
                for element in self.travesal( value ):
                    retVal.append( key + element )
            else:
                retVal.append( '' )

        return retVal

def main() :
    words = ["mass","as","asa", "abc", "hero","superhero"]

    trie = Trie()

    for word in words:
        trie.insert( word )

    print 'Travesal result:', trie.travesal(), '\n'

    print 'ab in the trie:', trie.search( 'ab' )
    print 'abc in the trie:', trie.search( 'abc' ), '\n'

    print 'her prefix in the trie:', trie.startswith( 'her' )
    print 'super prefix in the trie:', trie.startswith( 'super' )
    print 'has prefix in the trie:', trie.startswith( 'has' )

if __name__ == '__main__' :
    main()
