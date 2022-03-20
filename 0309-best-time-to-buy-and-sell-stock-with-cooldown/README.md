# Problem
[309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)

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
        rest = 0
        
        for price in prices:
            preHold, preSell = hold, sell
            preRest = rest
            
            hold = max(preHold, preRest - price)
            sell = preHold + price
            rest = max(preRest, preSell)
            
        return max(sell, rest)
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
     
    public int maxProfit(int[] prices) {
        /* base case */
        if(prices.length == 1) return 0;
        
        int hold = Integer.MIN_VALUE, noHold = 0;
        int preDaySell = 0;
        
        for(int price: prices) {
            int preHold = hold, preNoHold = noHold;
            
            hold   = Math.max(preHold,   preDaySell - price);
            noHold = Math.max(preNoHold, preHold    + price );
            
            preDaySell = preNoHold;
        }
        
        return noHold;
    }
}
```
