class Solution {
    /**  
     * @time  : O(n)
     * @space : O(n)
     */
    
    public int deepestLeavesSum(TreeNode root) {
        /* base case */
        if(root.left == null && root.right == null) return root.val;
        
        Queue<TreeNode> stack = new LinkedList<TreeNode>();
        stack.add(root);
        int ans = 0;
        
        while(!stack.isEmpty()) {
            ans = 0;
            
            int size = stack.size();
            for(int i=0 ; i<size ; i++) {
                TreeNode node = stack.remove();
                ans += node.val;
                
                if(node.left != null) stack.add(node.left);
                if(node.right != null) stack.add(node.right);
            }
        }
        
        return ans;
    }
}