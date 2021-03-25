class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        for num in range( 1, n+1 ):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            tmpStr = ""

            if divisible_by_3: tmpStr += "Fizz"
            if divisible_by_5: tmpStr += "Buzz"
            if not tmpStr: tmpStr = str( num )

            ans.append( tmpStr )

        return ans
