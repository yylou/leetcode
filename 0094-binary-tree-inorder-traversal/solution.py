##  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ##  (edge case) root is none, root has not children
        if not root: return []
        if not root.left and not root.right: return [root.val]

        ##  (1) iterative solution
        retVal = []
        stack = []
        curNode = root

        while stack or curNode:
            ##  keep visiting left node until achieve at the leaf
            while curNode:
                stack.append(curNode)
                curNode = curNode.left

            ##  pop out the last added node and append its value
            curNode = stack.pop()
            retVal.append(curNode.val)

            ##  assign the right node to the current node
            ##  --> checking end condition (if right node is none) or check the right branch
            curNode = curNode.right

        return retVal

        ##  ==================================================================================  ##

        ##  (2) recursive solution
        retVal = []

        def recursive(node, retVal):
            if node.left: recursive(node.left, retVal)
            retVal.append(node.val)
            if node.right: recursive(node.right, retVal)

        recursive(root, retVal)

        return retVal

        ##  ==================================================================================  ##

        ##  (3) recursive solution
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
