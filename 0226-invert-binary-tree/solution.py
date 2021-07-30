class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # (base case)
        if (not root) or (not root.left and not root.right): return root
        
        # ==================================================
        #  Binary Tree                       (Iterative)   =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        stack = [root]
        while stack:
            node = stack.pop()
                
            node.left, node.right = node.right, node.left
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            
        return root
            
        '''
        # ==================================================
        #  Tree                              (Recursive)   =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        '''