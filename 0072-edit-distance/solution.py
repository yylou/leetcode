##  dp 2d array record solution: bottom-up with recursion
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        ##  edge case handling: two words are empty
        if not word1 and not word2 : return 0

        len1, len2 = len( word1 ), len( word2 )

        ##  NOTE: cannot be '[[-1 for i in range( len1 )] for j in range( len2 )]'
        ##        since x index (index1) needs to represent word1
        dp_2d_array = [[-1 for i in range( len2 )] for j in range( len1 )]


        ##  helper function: compare the char and to the corresponding operations
        def dp( index1, index2 ) :
            ##  base case: if one reaches the end, return the remaining length of the other one
            if index1 == len1 : return len2 - index2
            if index2 == len2 : return len1 - index1

            if dp_2d_array[index1][index2] != -1 : return dp_2d_array[index1][index2]

            ##  if two chars are the same, move to the next char simultaneously
            if word1[index1] == word2[index2] :
                dp_2d_array[index1][index2] = dp( index1+1, index2+1 )

            else :
                ##  insert
                insert  = 1 + dp( index1 + 1, index2 )
                ##  delete
                delete  = 1 + dp( index1,     index2 + 1 )
                ##  replace
                replace = 1 + dp( index1 + 1, index2 + 1 )

                dp_2d_array[index1][index2] = min( insert, delete, replace )

            return dp_2d_array[index1][index2]


        return dp( 0, 0 )
