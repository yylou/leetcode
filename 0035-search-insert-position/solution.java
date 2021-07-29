class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
    
    public int searchInsert(int[] nums, int target) {
        /* base case */
        if(nums.length == 1) return (nums[0] >= target) ? 0 : 1;
        
        int l = 0, r = nums.length;
        while(l < r) {
            int mid = (l + r) / 2;
            
            if(nums[mid] == target) return mid;
            else if(nums[mid] > target) r = mid;
            else if(nums[mid] < target) l = mid + 1;
        }
        
        return l;
    }
}