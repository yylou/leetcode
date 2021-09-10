class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public int singleNumber(int[] nums) {
        int ret = 0;
        for(int num : nums) ret ^= num;
        return ret;
    }
}