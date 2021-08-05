public class Solution {
    /**
     * @time  : O(n^2)
     * @space : O(n)
     */
    
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        /* base case */
        if(nums.length == 0) return null;
        if(nums.length == 1) return new TreeNode(nums[0]);
        
        return construct(nums, 0, nums.length);
    }
    
    public TreeNode construct(int[] nums, int l, int r) {
        if (l >= r) return null;
        
        int max_i = max(nums, l, r);
        TreeNode root = new TreeNode(nums[max_i]);
        root.left = construct(nums, l, max_i);
        root.right = construct(nums, max_i + 1, r);
        return root;
    }
    
    public int max(int[] nums, int l, int r) {
        int max_i = l;
        for (int i = l; i < r; i++) {
            if (nums[max_i] < nums[i])
                max_i = i;
        }
        return max_i;
    }
}