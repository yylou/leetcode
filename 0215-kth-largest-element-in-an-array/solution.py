class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # (base case)
        if len(nums) == 1: return nums[0]
        
        # ==================================================
        #  Array + Quickselect (k largest = n-k smallest)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        self.nums = nums
        return self.quickSelect(0, len(nums) - 1, k - 1)
    
    def quickSelect(self, left, right, kLargest) -> int:
        while left <= right:
            pivot = self.partition(left, right)
            if pivot == kLargest: return self.nums[kLargest]
            elif pivot > kLargest: right = pivot - 1
            else: left = pivot + 1
                
    def partition(self, left, right) -> int:
        randomNum = (left + right) // 2
        
        #  move pivot to the end/right
        pivot = right
        self.nums[randomNum], self.nums[pivot] = self.nums[pivot], self.nums[randomNum]
        
        #  move all larger elements to the left
        placeP = left
        for i in range(left, right):
            if self.nums[i] >= self.nums[pivot]:
                self.nums[placeP], self.nums[i] = self.nums[i], self.nums[placeP]
                placeP += 1
            
        #  move back the pivot to make an almost-sorted array
        self.nums[placeP], self.nums[pivot] = self.nums[pivot], self.nums[placeP]
        return placeP
