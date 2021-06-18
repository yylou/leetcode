class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #: (base case)
        if len(nums) == 1: return TreeNode(nums[0])
        if len(nums) == 2: return TreeNode(nums[0], None, TreeNode(nums[1]))
        
        # ==================================================
        #  Tree + DFS + Recursion                          =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        def subTree(left, right) -> TreeNode:
            if left  > right: return None
            if left == right: return TreeNode(nums[left])
            
            center = (left + right) // 2
            
            node       = TreeNode(nums[center])
            node.left  = subTree(left, center - 1)
            node.right = subTree(center + 1, right)
            
            return node
            
        return subTree(0, len(nums)-1)
    
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */

    public TreeNode subTree(int left, int right) {
        if(left  > right) return null;
        if(left == right) return new TreeNode(nums[left]);
            
        int center = (left + right) / 2;
        
        TreeNode node = new TreeNode(nums[center]);
        node.left  = subTree(left, center - 1);
        node.right = subTree(center + 1, right);
        
        return node;
    }
    
    public TreeNode sortedArrayToBST(int[] nums) {
        /* base case */
        if(nums.length == 1) return new TreeNode(nums[0]);
        
        this.nums = nums;
        
        return subTree(0, nums.length - 1);
    }
}
==================================================================================================
'''
