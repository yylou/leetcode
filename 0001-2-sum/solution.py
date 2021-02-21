class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}

        for i in range( len( nums ) ) :
            remain = target - nums[i]

            ##  since there is only one exact solution, it has no problem to overwrite the record
            if remain not in hashTable :
                hashTable[nums[i]] = i
            else :
                return [i, hashTable[remain]]
