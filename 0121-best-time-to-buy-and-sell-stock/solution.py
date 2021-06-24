class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  (base case)
        if len(prices) == 1: return 0
        
        # ==================================================
        #  Array + Dynamic Programming         (localMin)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        localMin, maxProfit = float('inf'), float('-inf')
        for i in range(len(prices)):
            if prices[i] < localMin: localMin = prices[i]
                
            tmpProfit = prices[i] - localMin
            if tmpProfit > maxProfit: maxProfit = tmpProfit
                
        return maxProfit
        
        '''
        # ==================================================
        #  Array + Dynamic Programming         (localMax)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        localMax, maxProfit = float('-inf'), float('-inf')
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > localMax: localMax = prices[i]
            
            tmpProfit = localMax - prices[i]
            if tmpProfit > maxProfit: maxProfit = tmpProfit
                
        return maxProfit
        '''
        
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
     
    public int maxProfit(int[] prices) {
        /* base case */
        if(prices.length == 1) return 0;
        
        int localMin = Integer.MAX_VALUE, maxProfit = Integer.MIN_VALUE;
        for(int i=0 ; i<prices.length ; i++) {
            if(prices[i] < localMin) localMin = prices[i];
                
            int tmpProfit = prices[i] - localMin;
            if(tmpProfit > maxProfit) maxProfit = tmpProfit;
        }
        
        return maxProfit;
    }
}
==================================================================================================
'''
