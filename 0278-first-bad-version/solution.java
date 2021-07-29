/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
    
    public int firstBadVersion(int n) {
        /* base case */
        if (n == 1) return 1;
        
        int l = 1, r = n;
        while(l < r) {
            int mid = l + (r - l) / 2;
            
            if(isBadVersion(mid)) r = mid;
            else l = mid + 1;
        }
        
        return l;
    }
}