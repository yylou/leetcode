class Solution {
    /**
     * @time  : O(nlog(m)), m is the search space
     * @space : O(1)
     */
    
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 1000000000;
        while (l < r) {
            int m = (l + r) / 2, total = 0;
            for (int p : piles) total += (p - 1) / m + 1;
            
            if (total <= h) r = m;
            else l = m + 1;
        }
        return l;
    }
}