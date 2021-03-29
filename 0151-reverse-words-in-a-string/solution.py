class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        ##  Solution(1) two pointers without built-in functions support
        left, right = 0, len(s)-1

        ##  ignoring leading and trailing spaces
        while s[left] == ' ': left += 1
        while s[right] == ' ': right -= 1

        ##  find words and append into stack while skipping inner spaces
        stack = []
        while left <= right:
            word = ''

            if s[left] == ' ':
                left += 1
                continue

            while left <= right and s[left] != ' ':
                word += s[left]
                left += 1

            stack.append( word )
            word = ''

        ##  only one word, return directly
        if len(stack) == 1: return stack[0]

        ##  iterating stack reversely
        retString = ''
        for i in xrange( len(stack)-1, -1, -1 ): retString += stack[i] + ' '

        return retString[:len(retString)-1]


        # ======================================================================== #


        ##  Solution (2) split string then reverse by two pointers
        stack = s.split()
        n = len(stack)

        if n == 1: return stack[0]

        ##  reverse list
        left, right = 0, n-1
        while left < right:
            stack[left], stack[right] = stack[right], stack[left]
            left += 1
            right -= 1

        return ' '.join( stack )


        # ======================================================================== #


        ##  Solution (3) one-liner by python built-in reverse/split/join functions
        return ' '.join( reversed( s.split() ) )
