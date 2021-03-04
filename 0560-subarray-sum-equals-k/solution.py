class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ##  initialize for the sum that matches from the STARTING index
        hashTable = {0: 1}

        curSum = 0
        retVal = 0

        for num in nums:
            curSum += num

            ##  check whether REMAIN is recorded or not
            remain = curSum - k
            if remain in hashTable: retVal += hashTable[remain]

            ##  increasing the counter of accumulated sum
            if curSum in hashTable: hashTable[curSum] += 1
            else: hashTable[curSum] = 1

        return retVal
