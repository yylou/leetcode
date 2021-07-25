class Solution {
    /**  
     * @time  : O(n)
     * @space : O(n), O(log(n)) for average case
     */
    
    public int minDepth(TreeNode root) {
        /* base case */
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        int depth = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()) {
            int size = queue.size();
            for(int i=0 ; i<size ; i++) {
                TreeNode node = queue.remove();
                
                if(node.left == null && node.right == null) return depth + 1;
                
                if(node.left != null) queue.add(node.left);
                if(node.right != null) queue.add(node.right);
            }
            
            depth++;
        }
        
        return depth;
    }
}