class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        #:  (edge case)
        if s[0] == '0': return 0


        #:  Solution (1) iterative dp with 2 variable
        prev_1 = 1
        prev_2 = 1
        for i in xrange( 1, len(s) ):
            cur = 0
            if s[i] != '0': cur = prev_1
            if i > 0 and '09' < s[i-1:i+1] < '27': cur += prev_2

            prev_2 = prev_1
            prev_1 = cur

        return prev_1


        # =============================================================== #


        #:  Solution (2) iterative with dp table
        dp_table = [1] + [0 for _ in xrange( len(s) )]
        for i in xrange( 1, len(dp_table) ):
            #:  'assign' instead of 'accumulating' since one digit only has one solution
            if s[i-1] != '0':
                dp_table[i] = dp_table[i-1]

            if i > 1 and '09' < s[i-2:i] < '27':
                dp_table[i] += dp_table[i-2]

        print dp_table
        return dp_table[-1]


        # =============================================================== #


        #:  Solution (3) recursive with dp table
        dp_table = {}
        global dp_table


        def backTracking( index, string ):
            global dp_table

            if index in dp_table: return dp_table[index]

            if index == len( string ):
                return 1

            if string[index] == '0':
                return 0

            if index == len( string ) - 1:
                return 1

            ans = backTracking( index+1, string )

            if len(string[index:]) >= 2 and 0 < int( string[index:index+2] ) < 27:
                ans += backTracking( index+2, string )

            dp_table[index] = ans

            return ans


        return backTracking( 0, s )
