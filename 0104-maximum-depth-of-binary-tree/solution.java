class Solution {
    public int maxDepth(TreeNode root) {
        /* base case */
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        int maxDepth = 0;
        Queue<TreeNode> stack = new LinkedList<>();
        stack.add(root);
        
        while(!stack.isEmpty()) {
            int size = stack.size();
            
            for(int i=0 ; i<size ; i++) {
                TreeNode node = stack.remove();
                
                if(node.left != null) stack.add(node.left);
                if(node.right != null) stack.add(node.right);
            }
            
            maxDepth++;
        }
        
        return maxDepth;
    }
}