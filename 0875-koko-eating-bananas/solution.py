class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # ==================================================
        #  Binary Search                                   =
        # ==================================================
        # time  : O(nlog(m)), m is the search space
        # space : O(1)
        
        left, right = 1, max(piles)
        while left < right:
            speed = (left + right) // 2
            
            if sum(ceil(pile / speed) for pile in piles) <= h: right = speed
            else: left = speed + 1
        
        return left