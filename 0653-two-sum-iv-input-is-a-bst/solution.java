class Solution {
    /**  
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean findTarget(TreeNode root, int k) {
        HashSet<Integer> values = new HashSet<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if(values.contains(k - node.val)) return true;
            values.add(node.val);
            
            if(node.left != null) stack.push(node.left);
            if(node.right != null) stack.push(node.right);
        }
        
        return false;
    }
}