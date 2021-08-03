class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
        /* base case */
        if(p == null && q == null) return true;
        if(p == null || q == null) return false;
        if(p.val != q.val) return false;
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}