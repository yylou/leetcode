class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # (base case)
        if len(nums) == 1: return False

        # ==================================================
        #  Array + Hash Table (store value/index pairs)    =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        table = dict()

        for i in range(len(nums)):
            num = nums[i]

            if num in table and i - table[num] <= k:
                return True

            table[num] = i

        return False
