class Solution {
    /**  
     * @time  : O(n)
     * @space : O(1)
     */
    
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        
        while(l < r) {
            int tmp = numbers[l] + numbers[r];
            if(tmp == target) return new int[] {l+1, r+1};
            else if(tmp > target) r--;
            else if(tmp < target) l++;
        }
        
        return new int[] {-1, -1};
    }
}