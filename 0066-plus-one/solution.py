class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len( digits )

        ##  (edge case) only one digit, do the calculation directly
        if length == 1 :
            if digits[0] < 9 :
                digits[0] += 1
                return digits
            else :
                return [1, 0]

        carry = 1

        for i in range( length-1, -1, -1 ) :
            result = digits[i] + carry
            carry = result / 10

            ##  do not have to propagate --> BREAK
            if carry == 0 :
                digits[i] += 1
                break

            ##  need to proceed to the next digit
            else : digits[i] = 0

        if carry > 0 : digits.insert( 0, 1 )

        return digits
