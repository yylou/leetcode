# Problem
[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

# Performance
![result-python](./result.png)
![result-java](./result-java.png)

# Python
```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        # ==================================================
        #  [Array] DP                                      =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """
        
        # (base case)
        if len(prices) == 1: return 0
        
        hold, sell = float('-inf'), 0
        
        for price in prices:
            preHold, preSell = hold, sell
            
            hold = max(preHold, preSell - price)
            sell = max(preSell, preHold + price)
            
        return sell
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     * 
     * Greedy Method
     */
    
    public int maxProfit(int[] prices) {
        /* base case */
        if(prices.length == 1) return 0;
        
        int profit = 0;
        
        for( int i=1 ; i<prices.length ; i++) {
            int tmpProfit = prices[i] - prices[i-1];
            if(tmpProfit > 0) profit += tmpProfit;
        }
        
        return profit;
    }
}
```
