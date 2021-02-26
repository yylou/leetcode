##  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        lengthI = len(inorder)
        lengthP = len(postorder)

        ##  (edge case) tree only has one element
        if lengthP == 1 and lengthI == 1: return TreeNode(postorder[0])


        def recursive(key, node, postStart, postEnd, inStart, inEnd):
            ##  (debug)
            # print '\n', postorder[postStart:postEnd], inorder[inStart:inEnd],

            keyIndex = hashTable[key]

            ##  (debug)
            # print 'key:', key, 'index:', keyIndex

            nums = keyIndex - inStart

            ##  (end condition of Recursion) LEFT
            if keyIndex == inStart:
                node.left = None
            else:
                ##  (debug)
                # print 'left:', postorder[postStart:postStart+nums], inorder[inStart:keyIndex]

                ##  the target index is 1 SMALLER THAN as next preorder's END index
                node.left = TreeNode(postorder[postStart+nums-1])

                recursive(node.left.val, node.left, postStart, postStart+nums, inStart, keyIndex)

            ##  (end condition of Recursion) RIGHT
            if keyIndex == inEnd-1:
                node.right = None
            else:
                ##  (debug)
                # print 'right:', postorder[postStart+nums:postEnd-1], inorder[keyIndex+1:inEnd]

                ##  the target index is 1 SMALLER THAN as next preorder's END index
                node.right = TreeNode(postorder[postEnd-1-1])

                recursive(node.right.val, node.right, postStart+nums, postEnd-1, keyIndex+1, inEnd)


        hashTable = {}
        for index, value in enumerate(inorder):
            hashTable[value] = index

        ##  ROOT = LAST element in preorder
        root = TreeNode(postorder[-1])
        recursive(root.val, root, 0, lengthP, 0, lengthI)

        return root
