class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # (base case)
        if len(numbers) == 2: return [1, 2] if sum(numbers) == target else [-1, -1]
        
        # ==================================================
        #  Array + Two Pointer                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        l, r = 0, len(numbers) - 1
        while l < r:
            tmp = numbers[l] + numbers[r]
            if   tmp == target: return [l+1, r+1]
            elif tmp > target: r -= 1
            elif tmp < target: l += 1
                
        return [-1, -1]
        
        '''
        # ==================================================
        #  Binary Search                                   =
        # ==================================================
        # time  : O(nlog(n))
        # space : O(1)
        
        for i in range(len(numbers) - 1):
            l = i + 1
            r = len(numbers) - 1
            remain = target - numbers[i]
            
            while l <= r:
                mid = (l + r) // 2
                if   numbers[mid] == remain: return [i+1, mid+1]
                elif numbers[mid]  > remain: r = mid - 1
                elif numbers[mid]  < remain: l = mid + 1
                    
        return [-1, -1]
        '''