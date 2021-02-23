"""
##  Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        ## (edge case) root == none, root's children == none
        if not root: return []
        if not root.children: return [root.val]

        ##  (1) Iterative Solution
        retVal = []
        stack = [root]
        while stack:
            ##  (debug)
            # print map(lambda x: x.val, stack), retVal[::-1]

            ##  pop the last node added to the stack
            curNode = stack.pop()

            ##  REVERSLY append the children nodes of the popped node to the stack
            ##  [NOTE] to make the last node in the stack be the first child node
            if curNode.children: stack += curNode.children[::-1]

            ##  append popped node's value to the list
            retVal.append(curNode.val)

        return retVal

        ##  ==================================================================================  ##

        ##  (2) Recursive Solution
        retVal = [root.val]

        def recursive(node, retVal):
            retVal.append(node.val)

            if node.children:
                for childNode in node.children:
                    recursive( childNode, retVal )

        for node in root.children:
            recursive(node, retVal)

        return retVal
