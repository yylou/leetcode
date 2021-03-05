##  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_depth = 0

        ##  (edge case) root node is nullm root has no left and right children node
        if root == None : return 0
        elif root.left == None and root.right == None : return 1

        ##  (Solution 1) Iteratively visit in BFS manner
        
        ##  put node for visiting into a list
        record = [root]

        while record :
            ##  loop through the list to check the existence of right and left node
            for i in range( len( record ) ) :
                ##  visited, remove from the list
                cur_node = record.pop( 0 )

                ##  if child node is not null, append to the list
                if cur_node.right != None : record.append( cur_node.right )
                if cur_node.left  != None : record.append( cur_node.left  )

            max_depth += 1

        return max_depth

        # ============================================================================== #
        
        ##  (Solution 2) Recursively visit in DFS manner and compare the MAX depth (one-liners)
        return max( self.maxDepth( root.left ) + 1, self.maxDepth( root.right ) + 1 )
    
