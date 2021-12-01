class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()

        # ==================================================
        #  Array + Hash Table                              =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        for i in range(len(nums)):
            remain = target - nums[i]

            if remain in hashTable:
                return [i, hashTable[remain]]

            # We could overwrite since there is only one solution
            hashTable[nums[i]] = i
