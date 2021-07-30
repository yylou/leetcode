class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # (base case)
        if not root.left and not root.right: return True
        
        # ==================================================
        #  Tree + DFS + Stack                (Iterative)   =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            
            if node.val >= upper or node.val <= lower: return False
            
            # (left  sub-tree) set UPPER bound to current node's value (<= curValue)
            if node.left : stack.append( (node.left,  lower,    node.val) )

            # (right sub-tree) set LOWER bound to current node's value (>= curValue)
            if node.right: stack.append( (node.right, node.val, upper) )
                
        return True
    
    '''
    # ==================================================
    #  Tree + DFS + Stack                (Recursive)   =
    # ==================================================
    # time  : O(n)
    # space : O(n)

    def isValidBST(self, root: TreeNode) -> bool:
        # (base case)
        if not root.left and not root.right: return True

        return self._isValidBSTHelper(root, float('-inf'), float('inf'))

    def _isValidBSTHelper(self, node, lower, upper):
        if not node: return True

        if ((upper > node.val > lower)                              and
            self._isValidBSTHelper(node.left,  lower,    node.val ) and
            self._isValidBSTHelper(node.right, node.val, upper)):
            return True

        return False
    '''