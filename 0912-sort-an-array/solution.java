class Solution {
    public int[] sortArray(int[] nums) {
        return quickSort(nums);
        // return mergeSort(nums);
    }
    
    /**  
     * @time  : O(nlog(n))
     * @space : O(n)
     */
    public int[] mergeSort(int[] nums) {
        sortMerge(nums, 0, nums.length - 1);
        return nums;
    }
    
    private void sortMerge(int[] nums, int left, int right) {
        if(left < right) {
            int mid = (left + right) / 2;
            sortMerge(nums, left, mid);
            sortMerge(nums, mid + 1, right);
            merge(nums, left, mid, right);
        }
    }
    
    private void merge(int[] nums, int left, int mid, int right) {
        int[] ret = new int[right - left + 1];
        int p0 = 0, p1 = left, p2 = mid + 1;
        while(p1 <= mid && p2 <= right) {
            if(nums[p1] < nums[p2]) ret[p0++] = nums[p1++];
            else ret[p0++] = nums[p2++];
        }
        
        while(p1 <= mid) ret[p0++] = nums[p1++];
        while(p2 <= right) ret[p0++] = nums[p2++];
        
        for(int i=left ; i<=right ; i++) nums[i] = ret[i - left];
    }
    
    /**  
     * @time  : O(nlog(n))
     * @space : O(nlog(n))
     */
    public int[] quickSort(int[] nums) {
        sortQuick(nums, 0, nums.length);
        return nums;
    }
    
    private void sortQuick(int[] nums, int left, int right) {
        if(left == right || right - left == 1) return;
        
        int pivot = partition(nums, left, right - 1);
        sortQuick(nums, left, pivot);
        sortQuick(nums, pivot + 1, right);
    }
    
    private int partition(int[] nums, int left, int right) {
        int randomNum = (left + right) / 2;
        int pivot = right;
        
        int tmp = nums[randomNum];
        nums[randomNum] = nums[pivot];
        nums[pivot] = tmp;
        
        int placeP = left;
        for(int i=left ; i<right ; i++) {
            if(nums[i] <= nums[pivot]) {
                tmp = nums[placeP];
                nums[placeP] = nums[i];
                nums[i] = tmp;
                
                placeP++;
            }
        }
        
        tmp = nums[pivot];
        nums[pivot] = nums[placeP];
        nums[placeP] = tmp;
        
        return placeP;
    }
}