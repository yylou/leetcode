class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        ##  (edge case) nums only has 1 element
        length = len( nums )
        if length == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, length-1

        while left <= right:
            ##  BINARY SEARCH: find the middle point
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            ##  keep DIVIDING: check target is on the left or right side
            else:
                ##  (case) left-rotate: (2 3 4) [5] 6 7 1
                if nums[left] <= nums[mid]:
                    ##  in the left part (CONSECUTIVE numbers)
                    if target < nums[mid] and target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

                ##  (case) right-rotate: (5 6 7) [1] 2 3 4
                else:
                    ##  in the right part (CONSECUTIVE numbers)
                    if target > nums[mid] and target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

        return -1
