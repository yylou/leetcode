class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        # ==================================================
        #  Binary Search Tree + Stack                      =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        stack = [root]
        values = set()
        
        while stack:
            node = stack.pop()
            if k - node.val in values: return True
            values.add(node.val)
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return False