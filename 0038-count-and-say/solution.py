class Solution:
    def countAndSay(self, n: int) -> str:
        # (base case)
        if n == 1: return '1'
        
        # ==================================================
        #  String + Math                                   =
        # ==================================================
        # time  : O(nk)
        # space : O(1)
        
        ret = '1'
        
        for _ in range(n - 1):
            prev, counter = ret[0], 0
            tmp = ''
            
            for c in ret:
                if prev != c:
                    tmp += str(counter) + prev
                    prev, counter = c, 1
                else:
                    counter += 1
                    
            tmp += str(counter) + prev
            ret = tmp
            
        return ret