class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0

        answer = 0
        record = [1] * n
        record[0] = record[1] = 0


        #:  Solution (1) jump
        i = 2
        while i*i < n:  #:  only check a number if its square is less than n

            if record[i]:
                #:  mark all its multiples from i*i to n by 0.
                record[i*i::i] = [0] * ( 1 + ( (n - i*i - 1) // i ) )

            #:  increase i by 2 to skip EVEN number
            i += 1 if i == 2 else 2

        return sum( record )


        # ===================================================================== #


        #:  Solution (2) iterative
        answer = 0
        record = [False] * n
        for i in xrange( 2, n ):
            if record[i] == False:
                answer += 1

                tmp = 2
                while i*tmp < n:
                    record[i*tmp] = True
                    tmp += 1

        return answer
