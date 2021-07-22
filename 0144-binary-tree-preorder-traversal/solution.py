class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # (base case)
        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        # ==================================================
        #  Binary Tree + Pre-order Traversal               =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
                
        return ans
        
        '''
        # ==================================================
        #  Binary Tree + Pre-order Traversal               =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        '''