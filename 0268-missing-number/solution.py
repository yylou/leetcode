class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # ==================================================
        #  Math                                            =
        # ==================================================
        # time  : O(n) for SUM operation
        # space : O(1)

        total = sum(nums)
        expectSum = len(nums)*(len(nums) + 1) // 2
        return expectSum - total

        """
        # ==================================================
        #  Bit Manipulation                                =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        '''
        missing = 4 ∧ (0∧0) ∧ (1∧1) ∧ (2∧3) ∧ (3∧4)
                = (4∧4) ∧ (0∧0) ∧ (1∧1) ∧ (3∧3) ∧ 2
                = 0 ∧ 0 ∧ 0 ∧ 0 ∧ 2
                = 2
        '''

        ans = len(nums)

        for i in range(ans):
            ans ^= i ^ nums[i]

        return ans
        """

        """
        # ==================================================
        #  Array                                           =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        visited = [0] * (len(nums) + 1)

        for element in nums: visited[element] = 1

        for i in range(len(visited)):
            if not visited[i]: return i
        """
