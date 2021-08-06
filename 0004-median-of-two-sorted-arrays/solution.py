class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # ==================================================
        #  Array + Binary Seearch                          =
        # ==================================================
        # time  : O(log(min(m,n)))
        # space : O(1)
        
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        total = m + n
        size = (total + 1) // 2
        
        l, r = 0, len(nums1)
        while l <= r:
            p1 = (l + r) // 2
            p2 = size - p1
            
            nums1_left  = float('-inf') if p1 == 0 else nums1[p1 - 1]
            nums1_right = float('inf')  if p1 == m else nums1[p1]
            nums2_left  = float('-inf') if p2 == 0 else nums2[p2 - 1]
            nums2_right = float('inf')  if p2 == n else nums2[p2]
            
            if   nums1_left > nums2_right: r = p1 - 1
            elif nums2_left > nums1_right: l = p1 + 1
            else:
                if total & 1: return max(nums1_left, nums2_left)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2