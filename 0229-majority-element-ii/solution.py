class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #:  (edge case)
        n = len(nums)
        if n == 1: return nums


        #:  Solution (1) using hash table to record
        #:  - time complexity: O(n)
        #:  - space complexity: O(n)
        ans, counter, target = set(), dict(), n//3

        for element in nums:
            counter[element] = counter.get( element, 0 ) + 1

            if counter[element] > target:
                ans.add( element )
                if len(ans) == 2: return ans

        return ans


        # ======================================================================= #


        #: Solution (2) Boyer-Moore Voting Algorithm
        #:  - time complexity: O(n)
        #:  - space complexity: O(1)
        counter1, counter2, candidate1, candidate2 = 0, 0, None, None
        for num in nums:
            if num == candidate1: counter1 += 1
            elif num == candidate2: counter2 += 1
            elif counter1 == 0:
                candidate1 = num
                counter1 += 1
            elif counter2 == 0:
                candidate2 = num
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1

        ans = set()
        if nums.count( candidate1 ) > n//3: ans.add( candidate1 )
        if nums.count( candidate2 ) > n//3: ans.add( candidate2 )
        return ans
