class Solution {
    /**
     * @time  : O(n)
     * @space : O(H)
     */

    int count = 0;

    public int countUnivalSubtrees(TreeNode root) {
        /* base case */
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        dfs(root, root.val);
        return count;
    }
    
    private boolean dfs(TreeNode node, int val) {
        if (node == null)
            return true;
        
        boolean left  = dfs(node.left, node.val);
        boolean right = dfs(node.right, node.val);
        
        if(!left || !right)
            return false;
        
        count++;
        
        return node.val == val;
    }
}