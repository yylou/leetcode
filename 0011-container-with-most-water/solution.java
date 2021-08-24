class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
     
    public int maxArea(int[] height) {
        /* base case */
        if(height.length == 2) return Math.min(height[0], height[1]);
        
        int l = 0, r = height.length - 1;
        int area = 0;
            
        while(l < r) {
            int tmp = 0;
            
            if(height[l] < height[r]) {
                if(height[l] == 0) {
                    l += 1;
                    continue;
                }
                
                tmp = height[l] * (r - l);
                l += 1;
                
            } else {
                if(height[r] == 0) {
                    r -= 1;
                    continue;
                }
                
                tmp = height[r] * (r - l);
                r -= 1;
            }
            
            if(tmp > area) area = tmp;
        }
        
        return area;
    }
}