class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()

        # ==================================================
        #  Array + Hash Table                              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        for i in range( len(nums) ):
            remain = target - nums[i]
            
            if remain in hashTable:
                return [i, hashTable[remain]]
            
            #:  Since there is only one exact solution, it has no problem to overwrite the record
            hashTable[nums[i]] = i
