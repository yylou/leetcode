"""
##  Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        ##  (edge case) root is null, no children nodes
        if not root: return []
        if len(root.children) == 0: return[[root.val]]

        retVal = []
        stack = [root]

        ##  pop the parents and record, then append theirs children nodes into the stack
        while stack:
            tmpList = []
            for i in range( len(stack) ):
                ##  since the children nodes are stored in a list, need to POP FIRST element to keep the order
                curNode = stack.pop(0)
                tmpList.append(curNode.val)

                ##  APPEND to stack
                for element in curNode.children:
                    stack.append(element)

            ##  APPEND to answer (at the TAIL for TOP-DOWN approcach)
            retVal.append(tmpList)

        return retVal
