class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public List<List<Integer>> levelOrder(TreeNode root) {
        /* base case */
        if(root == null) return new ArrayList<>();
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        
        while(!queue.isEmpty()) {
            List<Integer> tmp = new ArrayList<Integer>();
            int size = queue.size();
            for(int i=0; i<size ; i++) {
                TreeNode node = queue.remove();
                tmp.add(node.val);
                
                if(node.left != null) queue.add(node.left);
                if(node.right != null) queue.add(node.right);
            }
            
            result.add(tmp);
        }
        
        return result;
    }
}