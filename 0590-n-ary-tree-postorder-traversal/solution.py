"""
##  Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        ##  (edge case) root == none, root.children == none
        if not root: return []
        if not root.children: return [root.val]

        ##  (1) Iterative Solution: REVERSELY preorder traversal with reversed answer
        retVal = []
        stack = [root]
        while stack:
            ##  (debug)
            # print map(lambda x: x.val, stack), retVal[::-1]

            ##  pop the last node added to the stack
            curNode = stack.pop()

            ##  append the children nodes of the popped node to the stack
            ##  then append the current
            if curNode.children:
                stack += curNode.children
                retVal.append(curNode.val)

            ##  append popped node's value to the list
            else: retVal.append(curNode.val)

        ##  REVERSE the answer
        return retVal[::-1]

        ##  ===========================================================================================  ##

        ##  (2) Iterative Solution
        retVal = []
        stack = [root]
        prevNode = None

        while stack:
            curNode = stack[-1]

            ##  (a) if children nodes == EMPTY --> pop from the stack
            ##  (b) previously visited node is in the current nodes' children nodes == visited done --> pop
            ##      since in the stack, parent node is next to its child node
            if not curNode.children or ( prevNode and prevNode in curNode.children ) :
                retVal.append( curNode.val )
                stack.pop()
                prevNode = curNode

                ##  (debug)
                # print map(lambda x: x.val, stack), retVal

            ##  REVERSELY append so that the last node is the left-most node
            else:
                stack += curNode.children[::-1]

                ##  (debug)
                # print map(lambda x: x.val, stack), retVal

        return retVal

        ##  ===========================================================================================  ##

        ##  (3) Recursive Solution: Postorder == REVERSELY preorder traversal with reversed answer
        retVal = [root.val]

        def recursive(node, retVal):
            retVal.append(node.val)

            if node.children:
                for childNode in node.children[::-1]:
                    recursive( childNode, retVal )

        for node in root.children[::-1]:
            recursive(node, retVal)

        return retVal[::-1]

        ##  ===========================================================================================  ##

        ##  (4) Recursive Solution: Postorder
        nullNode = Node(-1, [root])
        retVal = []

        def recursive(node, retVal):
            if node.children:
                for childNode in node.children:
                    recursive( childNode, retVal )
                retVal.append(node.val)
            else:
                retVal.append(node.val)

        for node in nullNode.children:
            recursive(node, retVal)

        return retVal
