##  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ##  (edge case) root is null, no children nodes
        if not root: return []
        if not root.left and not root.right: return[[root.val]]

        retVal = []
        stack = [root]

        ##  pop the parents and record, then append theirs children nodes into the stack
        while stack:
            tmpList = []
            for i in range( len(stack) ):
                ##  POP + RECORD
                curNode = stack.pop(0)
                tmpList.append( curNode.val )

                ##  APPEND to stack
                if curNode.left: stack.append(curNode.left)
                if curNode.right: stack.append(curNode.right)

            ##  APPEND to answer (at the TAIL for TOP-DOWN approcach)
            retVal.append(tmpList)

        return retVal
