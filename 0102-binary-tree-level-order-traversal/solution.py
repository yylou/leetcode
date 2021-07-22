class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # (base case)
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        
        # ==================================================
        #  Binary Tree + Level Order Traversal             =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        stack = [root]
        
        while stack:
            tmp = []
            for i in range(len(stack)):
                node = stack.pop(0)
                tmp.append(node.val)
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
            ans.append(tmp)
                    
        return ans