class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # ==================================================
        #  Math                                            =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        n, s = len(nums), sum(nums)
        dup = s - sum(set(nums))
        mis = (1+n) * n // 2 - (s - dup)

        return [dup, mis]

        """
        # ==================================================
        #  Negative Marking                                =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        dup, mis = None, None

        # Find NEG by value = DUP
        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0: dup = abs(num)
            else: nums[index] *= -1

        # Find POS by index = MIS
        for i in range(len(nums)):
            if nums[i] > 0: mis = i + 1

        return [dup, mis]
        """

        """
        # ==================================================
        #  Array + Hash Table                              =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        ans = [None, None]
        table = set()

        for num in nums:
            if num not in table: table.add(num)
            else: ans[0] = num

        for i in range(1, len(nums) + 1):
            if i not in table:
                ans[1] = i
                return ans
        """
