class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    int[] nums;
    
    public int findKthLargest(int[] nums, int k) {
        /* base case */
        if(nums.length == 1) return nums[0];
        
        this.nums = nums;
        return quickSelect(0, nums.length - 1, k - 1);
    }
    
    public int quickSelect(int left, int right, int k) {
        while(left <= right) {
            int pivot = partition(left, right);
            if(pivot == k) return this.nums[k];
            else if(pivot > k) right = pivot - 1;
            else left = pivot + 1;
        }
        
        return this.nums[k];
    }
    
    public int partition(int left, int right) {
        int randomNum = (left + right) / 2;
        int pivot = right;
        
        /* move pivot to the end/right */
        int tmp = this.nums[randomNum];
        this.nums[randomNum] = this.nums[pivot];
        this.nums[pivot] = tmp;
        
        /* move larger elements to the left */
        int placeP = left;
        for(int i=left ; i<right ; i++) {
            if(this.nums[i] >= this.nums[pivot]) {
                tmp = this.nums[i];
                this.nums[i] = this.nums[placeP];
                this.nums[placeP] = tmp;
                
                placeP++;
            }
        }
        
        /* move back pivot */
        tmp = this.nums[placeP];
        this.nums[placeP] = this.nums[pivot];
        this.nums[pivot] = tmp;
            
        return placeP;
    }
}
