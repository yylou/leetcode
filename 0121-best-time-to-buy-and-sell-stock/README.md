# Problem
[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

# Performance
![result-python](./result.png)
![result-java](./result-java.png)

# Python
```Python3
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
            
            hold = max(preHold, 0 - price)
            sell = max(preSell, preHold + price)
            
        return sell
```

```Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        # ==================================================
        #  [Array] DP                          (localMin)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """
 
        # (base case)
        if len(prices) == 1: return 0
        
        localMin, maxProfit = float('inf'), float('-inf')
        for i in range(len(prices)):
            if prices[i] < localMin: localMin = prices[i]
                
            tmpProfit = prices[i] - localMin
            if tmpProfit > maxProfit: maxProfit = tmpProfit
                
        return maxProfit
```

```Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        # ==================================================
        #  [Array] DP                          (localMax)  =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        """
       
        # (base case)
        if len(prices) == 1: return 0

        localMax, maxProfit = float('-inf'), float('-inf')
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > localMax: localMax = prices[i]
            
            tmpProfit = localMax - prices[i]
            if tmpProfit > maxProfit: maxProfit = tmpProfit
                
        return maxProfit
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
        
        int localMin = Integer.MAX_VALUE, maxProfit = Integer.MIN_VALUE;
        for(int price: prices) {
            if(price < localMin) localMin = price;
                
            int tmpProfit = price - localMin;
            if(tmpProfit > maxProfit) maxProfit = tmpProfit;
        }
        
        return maxProfit;
    }
}
```
