class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # (base case)
        if len(nums) == 1: return nums[0]

        # ==================================================
        #  Quickselect                                     =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        self.nums = nums
        self.quickSelect(0, len(nums) - 1, k - 1)
        return self.nums[k-1]

        # (Return top-k largest elements)
        # return self.nums[:k]

        """
        # ==================================================
        #  Heap                                            =
        # ==================================================
        # time  : O(nlog(k))
        # space : O(k)

        min_heap = []

        for i in range(k):
            heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])

        return min_heap[0]
        """

    def quickSelect(self, left, right, kLargest) -> None:
        if not (left < right): return

        pivot = self.partition(left, right)

        if pivot == kLargest: return
        elif pivot > kLargest: self.quickSelect(left, pivot-1, kLargest)
        else: self.quickSelect(pivot+1, right, kLargest)

    def partition(self, left, right) -> int:
        randomNum = (left + right) // 2

        # move pivot to the end/right
        pivot = right
        self.nums[randomNum], self.nums[pivot] = self.nums[pivot], self.nums[randomNum]

        # move larger elements to the left
        placeP = left
        for i in range(left, right):
            if self.nums[i] >= self.nums[pivot]:
                self.nums[placeP], self.nums[i] = self.nums[i], self.nums[placeP]
                placeP += 1

        # move back the pivot
        self.nums[placeP], self.nums[pivot] = self.nums[pivot], self.nums[placeP]
        return placeP
