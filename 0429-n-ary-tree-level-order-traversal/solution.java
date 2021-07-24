class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    List<List<Integer>> ans = new ArrayList<>();
    
    public List<List<Integer>> levelOrder(Node root) {
        /* base case */
        if(root == null) return ans;
        
        recursive(root, 0);
        return ans;
    }
    
    public void recursive(Node root, int level) {
        if(ans.size() == level) {
            ans.add(new ArrayList<>());
        }
        
        ans.get(level).add(root.val);
        
        for(Node node: root.children) {
            recursive(node, level + 1);
        }
    }
}