class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #:  (edge case)
        if len(nums) == 1: return nums[0]


        #:  Solution (1) Sort
        #:  - time complexity: O(nlogn)
        #:  - space complexity: O(1)
        nums.sort()
        return nums[len(nums) // 2]


        # ==================================================================== #


        #:  Solution (2) Boyer-Moore Voting Algorithm
        #:  - time complexity: O(n)
        #:  - space complexity: O(1)
        majority = ''
        count = 0
        for element in nums:
            if count == 0: majority = element
            count += 1 if element == majority else -1

        return majority


        # ==================================================================== #


        #:  Solution (3) use hash table to count
        #:  - time complexity: O(n)
        #:  - space complexity: O(n)
        counter = dict()
        for element in nums: counter[element] = counter.get( element, 0 ) + 1

        majority = ( '', -float( 'inf' ) )
        for key in counter:
            if counter[key] > majority[1]: majority = ( key, counter[key] )

        return majority[0]
