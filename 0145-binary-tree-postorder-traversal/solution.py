# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ## (edge case) root == none, root's children == none
        if not root: return []
        if not root.left and not root.right: return [root.val]

        ##  (1) Iterative solution:
        retVal = []
        stack = [root]
        prevNode = None

        while stack:
            ##  (debug)
            # print map(lambda x: x.val, stack), retVal[::-1]

            curNode = stack[-1]

            if ( not curNode.left and not curNode.right ) or ( prevNode and ( prevNode == curNode.right or prevNode == curNode.left ) ):
                retVal.append(curNode.val)
                stack.pop()
                prevNode = curNode

            else:
                if curNode.right: stack.append(curNode.right)
                if curNode.left: stack.append(curNode.left)

        return retVal

        ##  ==================================================================================  ##

        ##  (2) Iterative solution: REVERSE preorder traversal
        retVal = []
        stack = [root]

        while stack:
            ##  (debug)
            # print map(lambda x: x.val, stack), retVal[::-1]

            ##  APPEND the value at first, then traverse
            curNode = stack.pop()
            retVal.append(curNode.val)

            ##  append RIGHT at first due to the order of Python list data-structure
            if curNode.left: stack.append(curNode.left)
            if curNode.right: stack.append(curNode.right)

        return retVal[::-1]

        ##  ==================================================================================  ##

        ##  (3) recursive solution
        retVal = []

        def recursive(node, retVal):
            ##  TRAVERSE at first, then append the value
            if node.left: recursive(node.left, retVal)
            if node.right: recursive(node.right, retVal)

            retVal.append(node.val)

        recursive(root, retVal)

        return retVal
