class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    int[] nums;
    
    public TreeNode subTree(int start, int end) {
        if(start  > end) return null;
        if(start == end) return new TreeNode(nums[start]);
            
        int center = (start + end) / 2;
        
        TreeNode node = new TreeNode(nums[center]);
        node.left  = subTree(start, center - 1);
        node.right = subTree(center + 1, end);
        
        return node;
    }
    
    public TreeNode sortedArrayToBST(int[] nums) {
        /* base case */
        if(nums.length == 1) return new TreeNode(nums[0]);
        
        this.nums = nums;
        
        return subTree(0, nums.length - 1);
    }
}