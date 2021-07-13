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