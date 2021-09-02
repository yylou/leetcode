class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # (base case)
        if len(nums)  < 3: return []
        if len(nums) == 3: return [nums] if sum(nums) == 0 else []
        
        # ==================================================
        #  Math + Set                                      =
        # ==================================================
        # time  : O(n^2)
        # space : O(n) 
        
        zero, negative, positive = [], [], []
        for num in nums:
            if num > 0: positive.append(num)
            elif num < 0: negative.append(num)
            else: zero.append(num)
                
        # (case handling)
        if len(negative) == 0:
            if len(zero) == 0: return []
            if len(positive) == 0 and len(zero) < 3: return []
            if len(positive) == 0 and len(zero) == 3: return [[0, 0, 0]]
        
        ans = set()
        negSet = set(negative)
        posSet = set(positive)
        
        if len(zero) > 2: ans.add((0, 0, 0))
        
        # (-n, n, 0)
        if zero:
            for num in negSet:
                if -num in posSet: ans.add((num, -num, 0))
        
        # (-n, -m, n+m)
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                remain = -1 * (negative[i] + negative[j])
                if remain in posSet: ans.add(tuple(sorted([negative[i], negative[j], remain])))
        
        # (n, m, -n-m)
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                remain = -1 * (positive[i] + positive[j])
                if remain in negSet: ans.add(tuple(sorted([positive[i], positive[j], remain])))
                    
        return ans