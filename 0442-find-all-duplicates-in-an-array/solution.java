class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public List<Integer> findDuplicates(int[] nums) {
        /* base case */
        if(nums.length == 1) return new ArrayList<>();
        
        List<Integer> ans = new ArrayList<>();

        for(int num: nums) {
            int index = Math.abs(num) - 1;
            
            if(nums[index] > 0) nums[index] *= -1;
            else ans.add(Math.abs(num));
        }
        
        return ans;
    }
}
