##  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        lengthI = len(inorder)
        lengthP = len(preorder)

        ##  (edge case) tree only has one element
        if lengthP == 1 and lengthI == 1: return TreeNode(preorder[0])


        def recursive(key, node, preStart, preEnd, inStart, inEnd):
            ##  (debug)
            # print '\n', preorder[preStart:preEnd], inorder[inStart:inEnd],

            keyIndex = hashTable[key]

            ##  (debug)
            # print 'key:', key, 'index:', keyIndex

            nums = keyIndex - inStart

            ##  (end condition of Recursion) LEFT
            if keyIndex == inStart:
                node.left = None
            else:
                ##  (debug)
                # print 'left:', preorder[preStart+1:preStart+1+nums], inorder[inStart:keyIndex]

                ##  the target index is the SAME as next preorder's START index
                node.left = TreeNode(preorder[preStart+1])

                recursive(node.left.val, node.left, preStart+1, preStart+1+nums, inStart, keyIndex)

            ##  (end condition of Recursion) RIGHT
            if keyIndex == inEnd-1:
                node.right = None
            else:
                ##  (debug)
                # print 'right:', preorder[preStart+1+nums:lengthP], inorder[keyIndex+1:inEnd]

                ##  the target index is the SAME as next preorder's START index
                node.right = TreeNode(preorder[preStart+1+nums])

                recursive(node.right.val, node.right, preStart+1+nums, lengthP, keyIndex+1, inEnd)


        hashTable = {}
        for index, value in enumerate(inorder):
            hashTable[value] = index

        root = TreeNode(preorder[0])
        recursive(root.val, root, 0, lengthP, 0, lengthI)

        return root
