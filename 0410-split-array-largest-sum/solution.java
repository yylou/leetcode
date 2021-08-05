class Solution {
    /**
     * @time  : O(nlog(m)), m is the search space
     * @space : O(1)
     */
    
    public int splitArray(int[] nums, int m) {
        int l = 0, r = 0;
        for (int n: nums) {
            l = Math.max(l, n);
            r += n;
        }
        
        while(l < r) {
            int mid = (l + r) / 2;
            
            int count = 0, groups = 1;
            for(int n: nums) {
                count += n;
                if(count > mid) {
                    count = n;
                    groups += 1;
                }
                
                if(groups > m) break;
            }
            
            if(groups <= m) r = mid;
            else l = mid + 1;
        }
        
        return l;
    }
}