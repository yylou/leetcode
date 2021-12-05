class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        /* base case */
        if(nums.length == 1) return false;
        
        HashMap<Integer, Integer> table = new HashMap<>();
        
        for( int i=0 ; i<nums.length ; i++) {
            int num = nums[i];
            
            if(table.containsKey(num) && i - table.get(num) <= k) return true;
            
            table.put(num, i);
        }
        
        return false;
    }
}
