# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        # (base case)
        if n == 1: return 1
        if n == 2: return 1 if isBadVersion(1) else 2
        
        # ==================================================
        #  Binary Search                                   =
        # ==================================================
        # time  : O(log(n))
        # space : O(1)

        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            
            if isBadVersion(mid): r = mid
            else: l = mid + 1
                
        return l