##  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ## (edge case) root == none, root's children == none
        if not root: return []
        if not root.left and not root.right: return [root.val]

        ##  (1) Iterative solution
        retVal = []
        stack = [root]

        while stack:
            ##  (debug)
            # print map(lambda x: x.val, stack), retVal[::-1]

            ##  APPEND the value at then TRAVERSE
            curNode = stack.pop()
            retVal.append(curNode.val)

            ##  append RIGHT at first due to the order of Python list data-structure
            if curNode.right: stack.append(curNode.right)
            if curNode.left: stack.append(curNode.left)

        return retVal

        ##  ==================================================================================  ##

        ##  (2) recursive solution
        retVal = []

        def recursive(node, retVal):
            ##  APPEND the value at first, then traverse
            retVal.append(node.val)

            if node.left: recursive(node.left, retVal)
            if node.right: recursive(node.right, retVal)

        recursive(root, retVal)

        return retVal
    
        ##  ==================================================================================  ##

        ##  (3) recursive solution
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
