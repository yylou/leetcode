class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##  INTEGER RANGE = [0,n]

        ##  Solution (1) mathematical
        ##  - expected sum of list of positive integers with legnth 4: (4*5)/2 = 10
        ##  - test case: [1,3,2,4] (sum = 10, missing 0), [1,0,3,2] (sum = 6, missing 4)
        ##
        ##  - time complexity: O(n), due to SUM operation
        ##  - space complexity: O(1)
        curSum = sum( nums )
        return len(nums)*(len(nums)+1)//2 - curSum

        # ======================================================================================== #


        ##  Solution (2) using set to record, and iterate from 0 to length to find the missing number
        ##  - time complexity: O(n)
        ##  - space complexity: O(n)
        record = set(nums)

        for i in range( len(record) ):
            if i not in record: return i

        return len(record)
