class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # (base case)
        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        # ==================================================
        #  Binary Tree + Post-order Traversal              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    
        return ans
    
        '''
        # ==================================================
        #  Binary Tree + Post-order Traversal              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        '''