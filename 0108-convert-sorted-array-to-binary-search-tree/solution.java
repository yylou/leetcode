class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    int[] nums;
    
    public TreeNode subTree(int left, int right) {
        if(left  > right) return null;
        if(left == right) return new TreeNode(nums[left]);
            
        int center = (left + right) / 2;
        
        TreeNode node = new TreeNode(nums[center]);
        node.left  = subTree(left, center - 1);
        node.right = subTree(center + 1, right);
        
        return node;
    }
    
    public TreeNode sortedArrayToBST(int[] nums) {
        /* base case */
        if(nums.length == 1) return new TreeNode(nums[0]);
        
        this.nums = nums;
        
        return subTree(0, nums.length - 1);
    }
}