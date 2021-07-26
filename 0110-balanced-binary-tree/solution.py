class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # (base case)
        if not root: return True
        if not root.left and not root.right: return True
            
        # ==================================================
        #  Binary Tree + DFS                  (Bottom-up)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        return self.dfs(root) != -1
    
    def dfs(self, node: TreeNode) -> bool:
        if not node: return 0
        if not node.left and not node.right: return 1
        
        leftH = self.dfs(node.left)
        if leftH == -1: return -1
        
        rightH = self.dfs(node.right)
        if rightH == -1: return -1
        
        if abs(leftH - rightH) > 1: return -1
        return max(leftH, rightH) + 1
        
    '''
    def isBalanced(self, root: TreeNode) -> bool:
        # (base case)
        if not root: return True
        if not root.left and not root.right: return True
        
        # ==================================================
        #  Binary Tree                         (Top-down)  =
        # ==================================================
        # time  : O(nlog(n))
        # space : O(n)
            
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)
            
    def getHeight(self, root) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    '''