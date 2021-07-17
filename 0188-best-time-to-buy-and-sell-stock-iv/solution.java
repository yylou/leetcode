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