class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        # (base case)
        if not root: return 0
        if not root.left and not root.right: return 1
        
        # ==================================================
        #  Binary Search Tree + DFS                        =
        # ==================================================
        # time  : O(n)
        # space : O(H)

        self.unival = 0
        self.dfs(root, root.val)
        
        return self.unival
        
    def dfs(self, node: TreeNode, preVal: int) -> bool:
        if not node: return True
        
        left  = self.dfs(node.left,  node.val)
        right = self.dfs(node.right, node.val)
        
        if not left or not right:
            return False
        
        self.unival += 1
        
        return node.val == preVal
        