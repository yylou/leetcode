class Solution(object):
    def insertChar(self, node, chars):
        if node.keys() :
            for key in node : self.insertChar( node[key], chars )
        else :
            for char in chars : node[char] = {}


    def traverse(self, node, string, ret_value):
        if node.keys() :
            for key in node :
                tmpString = string + key
                self.traverse( node[key], tmpString, ret_value )
        else :
            ret_value.append( string )


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        record = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ##  (edge case) empty string, only one char in the string
        if not digits : return []
        if len( digits ) == 1 : return record[digits[0]]

        treeHead = {}

        ##  (Trie Solution) using Trie to store the possible char combination, then do DFS to collect the answer

        ##  insert char mapped with digit into tree
        for digit in digits : self.insertChar( treeHead , record[digit] )

        ret_value = []

        ##  DFS to collect the answers
        self.traverse( treeHead , '', ret_value )

        return ret_value
