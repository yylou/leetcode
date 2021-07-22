class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public List<Integer> preorderTraversal(TreeNode root) {
        /* base case */
        if(root == null) return new ArrayList<>();
        
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            result.add(node.val);
            
            if(node.right != null) stack.push(node.right);
            if(node.left != null) stack.push(node.left);
        }
        
        return result;
    }
}