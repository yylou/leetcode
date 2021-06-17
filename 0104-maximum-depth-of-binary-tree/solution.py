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
    
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #: (base case)
        if not root: return 0
        if not root.left and not root.right: return 1
        
        # ==================================================
        #  Binary Tree                       (Recursive)   =
        # ==================================================
        # time  : O(n)
        # space : O(n), O(log(n)) for average case
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
        '''
        # ==================================================
        #  Binary Tree                       (Iterative)   =
        # ==================================================
        # time  : O(n)
        # space : O(n), O(log(n)) for average case

        maxDepth = 0
        stack = [root]
        
        #: (level-order iterative solution)
        while stack:
            #: loop through stack for current length, pop the first node
            for i in range(len(stack)):
                node = stack.pop( 0 )
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
            maxDepth += 1
            
        return maxDepth
        '''
        
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n), O(log(n)) for average case
     */

    public int maxDepth(TreeNode root) {
        /* base case */
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        int maxDepth = 0;
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.add(root);
        
        while(!stack.isEmpty()) {
            int size = stack.size();
            
            for(int i=0 ; i<size ; i++) {
                TreeNode node = stack.pollFirst();
                
                if(node.left != null) stack.add(node.left);
                if(node.right != null) stack.add(node.right);
            }
            
            maxDepth++;
        }
        
        return maxDepth;
    }
}
==================================================================================================
'''
