class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # (base case)
        if len(nums) == 1: return []

        # ==================================================
        #  Negative Marking                                =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        ans = []

        for i in range(len(nums)):
            num = abs(nums[i]) - 1

            if nums[num] < 0: ans.append(num + 1)
            else: nums[num] *= -1

        return ans

        """
        # ==================================================
        #  Counter / Hash Table                            =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        counter = Counter(nums)
        res = list()
        for k, v in counter.items():
            if v == 2: res.append(k)
        return res
        """
