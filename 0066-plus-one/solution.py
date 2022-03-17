class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        """
        # ==================================================
        #  [Array] Math                                    =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """

        # (base case) Only one digit
        if len(digits) == 1: return [1, 0] if digits[0] == 9 else [digits[0] + 1]

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry

            carry = total // 10
            digits[i] = total % 10

            # No need to further progagate
            if not carry: return digits

        if carry: return [1] + digits
        return digits
