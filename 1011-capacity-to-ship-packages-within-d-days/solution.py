class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # ==================================================
        #  Binary Search                                   =
        # ==================================================
        # time  : O(nlog(m)), m is the search space
        # space : O(1)
        
        maxWeight, total = 0, 0
        for w in weights:
            total += w
            maxWeight = max(maxWeight, w)
        
        l, r = maxWeight, total
        while l < r:
            capacity = (l + r) // 2
            if self.valid(weights, days, capacity): r = capacity
            else: l = capacity + 1
            
        return l
    
    def valid(self, weights: List[int], D: int, capacity: int) -> bool:
        days, total = 1, 0
        for w in weights:
            total += w
            if total > capacity:
                total = w
                days += 1
                
                if days > D: return False
                
        return True