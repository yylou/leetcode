class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public int maxDepth(Node root) {
        /* base case */
        if(root == null) return 0;
        if(root.children == null) return 1;
        
        int maxDepth = 0;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()) {
            int size = queue.size();
            for(int i=0 ; i<size ; i++) {
                Node node = queue.remove();
                
                if(node.children != null) {
                    for(Node element: node.children) queue.add(element);
                }
            }
            
            maxDepth++;
        }
        
        return maxDepth;
    }
}