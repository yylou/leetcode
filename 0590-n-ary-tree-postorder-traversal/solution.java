class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    LinkedList<Integer> ans;
    
    public List<Integer> postorder(Node root) {
        ans = new LinkedList<Integer>();
        
        /* base case */
        if(root == null) return ans;
        
        recursive(root);
        return ans;
    }
    
    public void recursive(Node root) {
        if(root.children != null ){
            for(Node node: root.children) {
                recursive(node);
            }
        }
        
        ans.add(root.val);
    }
}