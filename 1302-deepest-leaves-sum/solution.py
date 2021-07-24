class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # (base case)
        if not root.left and not root.right: return root.val
        
        # ==================================================
        #  Binary Tree + Level Order Traversal             =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = 0
        stack = [root]
        
        while stack:
            ans = 0
            
            # loop through stack for current length, pop the first node
            for i in range(len(stack)):
                node = stack.pop(0)
                ans += node.val
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
        return ans