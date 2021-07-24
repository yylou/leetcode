class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */

    public TreeNode invertTree(TreeNode root) {
        if((root == null) || (root.left == null && root.right == null)) return root;
        
        TreeNode tmp = root.left;
        root.left  = root.right;
        root.right = tmp;
           
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
}