class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        # ==================================================
        #  Binary Search                                   =
        # ==================================================
        # time  : O(nlog(m)), m is the search space
        # space : O(1)
        
        l, r = max(nums), sum(nums)
        
        while l < r:
            mid = (l + r) // 2
            
            count, groups = 0, 1
            for num in nums:
                count += num
                if count > mid:
                    count = num
                    groups += 1
                    
                if groups > m: break
                    
            if groups <= m: r = mid
            else: l = mid + 1
            
        return l