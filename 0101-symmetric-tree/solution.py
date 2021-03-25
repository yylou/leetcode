##  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        ##  (edge case) basic check
        if not root.left and not root.right: return True
        if root.left and not root.right: return False
        if not root.left and root.right: return False
        if root.left.val != root.right.val: return False


        ##  Solution (1) recursive solution (preoder traversal)
        resultL, resultR = [], []

        def preorderL( node, result ):
            result.append( node.val )

            if node.left: preorderL( node.left, result )
            else: result.append( '' )

            if node.right: preorderL( node.right, result )
            else: result.append( '' )

        def preorderR( node, result ):
            result.append( node.val )

            if node.right: preorderR( node.right, result )
            else: result.append( '' )

            if node.left: preorderR( node.left, result )
            else: result.append( '' )

        preorderL( root.left, resultL )
        preorderR( root.right, resultR )

        return resultL == resultR


        # =========================================================================== #


        ##  Solution (2) iterative solution (preoder traversal)
        resultL, resultR = [], []
        stackL, stackR = [root.left], [root.right]
        while stackL:
            node = stackL.pop()
            if node == '': resultL.append( node )
            else:
                resultL.append( node.val )

                if node.right: stackL.append( node.right )
                else: stackL.append( '' )

                if node.left: stackL.append( node.left )
                else: stackL.append( '' )

        while stackR:
            node = stackR.pop()
            if node == '':
                resultR.append( node )
            else:
                resultR.append( node.val )

                if node.left: stackR.append( node.left )
                else: stackR.append( '' )

                if node.right: stackR.append( node.right )
                else: stackR.append( '' )

        return resultL == resultR


        # =========================================================================== #


        ##  Solution (3) compare and traverse at the same time (recursive)
        def check( left, right ):
            if left and right:
                return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)

            if not left and not right: return True
            return False

        return check( root.left, root.right )


        # =========================================================================== #


        ##  Solution (4) compare and traverse at the same time (iterative)
        stack = [root.left, root.right]
        while stack:
            nodeR = stack.pop()
            nodeL = stack.pop()

            if not nodeR and not nodeL: continue
            if (nodeR and not nodeL) or (not nodeR and nodeL): return False

            if nodeR.val != nodeL.val: return False

            stack.append( nodeL.left )
            stack.append( nodeR.right )
            stack.append( nodeL.right )
            stack.append( nodeR.left )

        return True
