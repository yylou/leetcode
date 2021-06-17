class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #: (base case)
        if not root: return 0
        if not root.left and not root.right: return 1
        
        # ==================================================
        #  Binary Tree                       (Recursive)   =
        # ==================================================
        # time  : O(n)
        # space : O(n), O(log(n)) for average case
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
        '''
        # ==================================================
        #  Binary Tree                       (Iterative)   =
        # ==================================================
        # time  : O(n)
        # space : O(n), O(log(n)) for average case

        maxDepth = 0
        stack = [root]
        
        #: (level-order iterative solution)
        while stack:
            #: loop through stack for current length, pop the first node
            for i in range(len(stack)):
                node = stack.pop( 0 )
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
            maxDepth += 1
            
        return maxDepth
        '''
        
'''
Java Solution
==================================================================================================
class Solution {
    public int maxDepth(TreeNode root) {
        /* base case */
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        int maxDepth = 0;
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.push(root);
        
        while(!stack.isEmpty()) {
            int size = stack.size();
            
            for(int i=0 ; i<size ; i++) {
                TreeNode node = stack.pollLast();
                
                if(node.left != null) stack.push(node.left);
                if(node.right != null) stack.push(node.right);
            }
            
            maxDepth++;
        }
        
        return maxDepth;
    }
}
==================================================================================================
'''
