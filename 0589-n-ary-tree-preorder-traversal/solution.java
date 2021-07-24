class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    LinkedList<Integer> answer;
    
    public List<Integer> preorder(Node root) {
        answer = new LinkedList<Integer>();
        
        /* base case */
        if(root == null) return answer;
        
        answer.add(root.val);
        
        if(root.children == null) return answer;
        
        for(Node node: root.children) {
            recursive(node);
        }
        
        return answer;
    }
    
    public void recursive(Node root) {
        answer.add(root.val);
        
        if(root.children != null ) {
            for(Node node: root.children) {
                recursive(node);
            }
        }
    }
}