# Problem
[714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
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
            sell = max(preSell, preHold + price - fee)
            
        return sell
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int maxProfit(int[] prices, int fee) {
        /* base case */
        if(prices.length == 1) return 0;
        
        int hold = -prices[0], noHold = 0;
        
        for(int i=1 ; i<prices.length ; i++) {
            int preHold = hold, preNoHold = noHold;
            
            hold   = Math.max(preHold,   preNoHold - prices[i]);
            noHold = Math.max(preNoHold, preHold   + prices[i] - fee);
        }
        
        return noHold;
    }
}
```
