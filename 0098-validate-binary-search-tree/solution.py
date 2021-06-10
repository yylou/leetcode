#: Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #: (edge case)
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
            
            #: (left  sub-tree) set UPPER bound to current node's value (<= curValue)
            #: (right sub-tree) set LOWER bound to current node's value (>= curValue)
            if node.left : stack.append( (node.left,  lower,    node.val) )
            if node.right: stack.append( (node.right, node.val, upper) )
                
        return True
    
    '''
    # ==================================================
    #  Tree + DFS + Stack                (Recursive)   =
    # ==================================================
    # time  : O(n)
    # space : O(n)

    def _isValidBSTHelper(self, node, lower, upper):
        if not node: return True

        if ((node.val > lower and node.val < upper)                 and
            self._isValidBSTHelper(node.left,  lower,    node.val ) and
            self._isValidBSTHelper(node.right, node.val, upper)):
            return True

        return False

    def isValidBST(self, root: TreeNode) -> bool:
        #: (edge case)
        if not root.left and not root.right: return True

        return self._isValidBSTHelper(root, float('-inf'), float('inf'))
    '''

'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public boolean isValidBST(TreeNode root) {
        
    }
}
==================================================================================================
'''
