class Solution(object):
    def insertParenthese(self, string):
        ret_value = set()

        for i in xrange( len(string) ) : ret_value.add( string[:i] + '()' + string[i:] )

        return ret_value

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ret_value = ['()']

        for i in xrange(n-1) :
            result = set()

            ##  insert '()' in each index of string
            ##  then using SET JOIN to combine without duplicate items
            for string in ret_value : result |= self.insertParenthese( string )

            ret_value = result

        return ret_value
