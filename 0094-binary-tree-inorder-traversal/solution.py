class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # (base case)
        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        # ==================================================
        #  Binary Tree + In-order Traversal               =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ret = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                ret.append(node.val)
                
            else:
                if node.right: stack.append((node.right, False))
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
            
        return ret

        '''
        # ==================================================
        #  Binary Tree + In-order Traversal               =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        '''