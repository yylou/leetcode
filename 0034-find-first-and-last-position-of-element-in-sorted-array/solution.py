class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # (base case)
        if not nums or (len(nums) == 1 and nums[0] != target): return [-1, -1]

        # ==================================================
        #  Two-pass Binary Search                          =
        # ==================================================
        # time  : O(log(n))
        # space : O(1)

        self.nums, start, end = nums, 0, 0

        start = self.binarySearch(target)
        end   = self.binarySearch(target+1) - 1

        return [start, end] if start <= end else [-1, -1]

    def binarySearch(self, target):
        """
        Find the position to insert target number to keep list sorted
        """

        l, r = 0, len(self.nums)
        while l < r:
            mid = (l + r) // 2

            if self.nums[mid] >= target: r = mid
            else: l = mid + 1

        return l

'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */

    public int[] searchRange(int[] nums, int target) {
        /* base case */
        if(nums.length == 0) return new int[]{-1, -1};

        int start = 0, end = 0;

        /* starting position (left-most element) */
        start = binarySearch(nums, target);
        end   = binarySearch(nums, target+1) - 1;

        if(start > end) return new int[]{-1, -1};
        return new int[]{start, end};
    }

    public int binarySearch(int[] nums, int target) {
        /* Find the position to insert target number to keep list sorted */
        int l = 0, r = nums.length;
        while(l < r){
            int mid = (l + r) / 2;

            if(nums[mid] >= target) r = mid;
            else l = mid + 1;
        }

        return l;
    }
}
=================================================================================================
'''
