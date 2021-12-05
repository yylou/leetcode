class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # (base case)
        if len(nums) == 1: return False

        # ==================================================
        #  Array + Set                                     =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        table = set()

        for num in nums:
            if num not in table: table.add(num)
            else: return True

        return False

        """
        # ==================================================
        #  One-liner                                       =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        return len(nums) != len(set(nums))
        """

        """
        # ==================================================
        #  Quick Sort                                      =
        # ==================================================
        # time  : O(nlogn)
        # space : O(logn)

        sorted_array = self.quickSort(nums)
        for i in range(0, len(sorted_array)-1):
            if sorted_array[i] == sorted_array[i+1]: return True
        return False
        """

    def quickSort(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1: return nums

        pivot = nums[len(nums) // 2]
        lt, eq, lg = list(), list(), list()
        for num in nums:
            if   num == pivot: eq += [num]
            elif num  > pivot: lg += [num]
            else: lt += [num]

        return self.quickSort(lt) + eq + self.quickSort(lg)
