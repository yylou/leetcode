class Solution {
    /**  
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean isBalanced(TreeNode root) {
        /* base case */
        if(root == null) return true;
        if(root.left == null && root.right == null) return true;
        
        return (dfs(root) != -1) ? true : false;
    }
    
    public int dfs(TreeNode root) {
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        int leftH = dfs(root.left);
        if(leftH == -1) return -1;
        
        int rightH = dfs(root.right);
        if(rightH == -1) return -1;
        
        if(Math.abs(leftH - rightH) > 1) return -1;
        return Math.max(leftH, rightH) + 1;
    }
}