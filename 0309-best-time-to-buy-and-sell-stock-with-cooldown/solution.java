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