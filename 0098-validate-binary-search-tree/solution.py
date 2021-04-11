#:  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        #:  (edge case)
        if not root.left and not root.right: return True


        #:  Solution (1) iterative in-order traversal
        stack = []
        curNode = root
        bound = -float('inf')

        while stack or curNode:
            if not curNode:
                curNode = stack.pop()
                if curNode.val <= bound: return False
                bound = curNode.val

                curNode = curNode.right

            else:
                stack.append( curNode )
                curNode = curNode.left


        # ===================================================================== #


        #:  Solution (2) iterative
        stack = [(root, float('inf'), -float('inf'))]
        while stack:
            node, upper, lower = stack.pop()

            val = node.val
            if val >= upper or val <= lower: return False

            if node.right: stack.append( (node.right, upper, val) )
            if node.left: stack.append( (node.left, val, lower) )

        return True
