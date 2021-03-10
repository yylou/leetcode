class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ##  (edge case) nums == null
        if not nums: return [-1, -1]

        ##  (edge case) length == 1
        length = len( nums )
        if length == 1:
            if nums[0] != target: return [-1, -1]
            else: return [0, 0]

        # ============================================
        #  BINARY SEARCH                             =
        # ============================================
        left, right = 0, length-1

        ##  ALL MATCH
        if nums[left] == target and nums[right] == target: return [left, right]

        ##  for LEFT-most
        ##  5  7  [7]  8  8  10  (8), return left = mid + 1
        while left <= right:
            mid = (left+right) // 2

            if target > nums[mid]: left = mid + 1
            else: right = mid - 1

        start = left
        left, right = 0, length-1

        ##  for RIGHT-most
        ##  5  7  7  8  8  [10]  (8), return right = mid - 1
        while left <= right:
            mid = (left+right) // 2

            if target >= nums[mid]: left = mid + 1
            else: right = mid -1

        end = right

        if start > end: return [-1, -1]
        return [start, end]
