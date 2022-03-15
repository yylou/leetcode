class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # ==================================================
        #  Array + Hash Table                              =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        table = dict()
        for i in range(len(nums)):
            remain = target - nums[i]

            if remain in table:
                return [i, table[remain]]

            # We could overwrite since there is only one solution
            table[nums[i]] = i
