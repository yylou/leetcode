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
