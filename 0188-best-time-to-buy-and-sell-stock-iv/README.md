# Problem
[188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

# Performance
![result-python](./result.png)
![result-java](./result-java.png)

# Python
```Python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # (base case)
        if len(prices) == 0 or len(prices) == 1: return 0

        # ==================================================
        #  Array + Dynamic Programming              (FSM)  =
        # ==================================================
        # time  : O(n*k)
        # space : O(k)
        
        # '+1' for day 0 initialization
        T = k + 1
        hold, noHold = [float('-inf')] * T, [0] * T
        
        for price in prices:
            for i in range(1, T):
                prevHold, prevNoHold = hold[i], noHold[i]
                
                hold[i]   = max(prevHold,   noHold[i-1] - price)
                noHold[i] = max(prevNoHold, prevHold    + price)
                
        return noHold[-1]
```

# Java
```Java
class Solution {
    public int maxProfit(int k, int[] prices) {
        /* base case */
        if(prices.length == 0 || prices.length == 1) return 0;
        
        int T = k + 1;
        
        int[] hold = new int[T], noHold = new int[T];
        Arrays.fill(hold,   Integer.MIN_VALUE);
        Arrays.fill(noHold, 0);
        
        for(int price: prices) {
            for(int i=1 ; i<T ; i++) {
                int preHold = hold[i], preNoHold = noHold[i];
                
                hold[i]   = Math.max(preHold,   noHold[i-1] - price);
                noHold[i] = Math.max(preNoHold, preHold     + price);
            }
        }
        
        return noHold[T - 1];
    }
}
}
```