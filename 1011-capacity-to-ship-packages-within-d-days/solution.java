class Solution {
    /**
     * @time  : O(nlog(m)), m is the search space
     * @space : O(1)
     */
    
    public int shipWithinDays(int[] weights, int days) {
        /* base case */
        if(weights.length == 1) return 1;
        
        int left = 0, right = 0;
        for (int w: weights) {
            left = Math.max(left, w);
            right += w;
        }
        
        while(left < right) {
            int capacity = (left + right) / 2;
                
            int tmpDays = 1, tmpWeight = 0;
            for(int w: weights) {
                tmpWeight += w;
                if(tmpWeight > capacity) {
                    tmpWeight = w;
                    tmpDays += 1;
                    
                    if(tmpDays > days) break;
                }
            }
            
            if(tmpDays <= days) right = capacity;
            else left = capacity + 1;
        }
        
        return left;
    }
}