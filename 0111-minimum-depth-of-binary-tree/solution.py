class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # (base case)
        if not root: return 0
        if not root.left and not root.right: return 1
        
        # ==================================================
        #  Binary Tree + Level Order Traversal             =
        # ==================================================
        # time  : O(n)
        # space : O(n), O(log(n)) for average case

        minDepth = 0
        stack = [root]
        
        while stack:
            # loop through stack for current length, pop the first node
            for i in range(len(stack)):
                node = stack.pop(0)
                
                if not node.left and not node.right: return minDepth + 1
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
            minDepth += 1
            
        return minDepth