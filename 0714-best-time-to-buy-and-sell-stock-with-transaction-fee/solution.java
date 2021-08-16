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