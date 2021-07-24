class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
     
    public boolean isValid(TreeNode node, long lower, long upper) {
        if(node == null) return true;
        
        return (lower < node.val && node.val < upper) &&
               isValid(node.left, lower, node.val)    && 
               isValid(node.right, node.val, upper);
    }
    
    public boolean isValidBST(TreeNode root) {
        if(root.left == null && root.right == null) return true;
        
        return isValid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}