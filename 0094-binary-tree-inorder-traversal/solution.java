class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */

    public List<Integer> inorderTraversal(TreeNode root) {
        /* base case */
        if(root == null) return new ArrayList<>();
        
        List<Integer> result = new ArrayList<>();
        Stack<Pair<TreeNode, Boolean>> stack = new Stack<Pair<TreeNode, Boolean>>();
        stack.push(new Pair<TreeNode, Boolean>(root, false));
        
        while(!stack.isEmpty()) {
            Pair<TreeNode, Boolean> object = stack.pop();
            TreeNode node = object.getKey();
            Boolean visited = object.getValue();
            
            if(visited == true) result.add(node.val);
            else {
                if(node.right != null) stack.push(new Pair<TreeNode, Boolean>(node.right, false));
                stack.push(new Pair<TreeNode, Boolean>(node, true));
                if(node.left != null) stack.push(new Pair<TreeNode, Boolean>(node.left, false));
            }
        }
        
        return result;
    }
}