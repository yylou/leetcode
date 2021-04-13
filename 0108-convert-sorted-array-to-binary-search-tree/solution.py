#:  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        #:  (edge case)
        if len(nums) == 1: return TreeNode( nums[0] )

        def subtree( left, right ):
            if left > right: return None
            if left == right: return TreeNode( nums[left] )

            center = (left + right) // 2

            node = TreeNode( nums[center] )
            node.right = subtree( center+1, right )
            node.left = subtree( left, center-1 )

            return node

        return subtree( 0, len(nums)-1 )
