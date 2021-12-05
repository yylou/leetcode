class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int missingNumber(int[] nums) {
        int total = 0;
        for(int num: nums) total += num;
        int expectedSum = nums.length * (nums.length + 1) / 2;
        
        return expectedSum - total;
    }
}
