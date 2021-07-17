class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # (base case)
        if len(nums) == 1: return TreeNode(nums[0])
        if len(nums) == 2: return TreeNode(nums[0], None, TreeNode(nums[1]))
        
        # ==================================================
        #  Binary Search Tree + Inorder Traversal          =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        self.nums = nums
        return self.subTree(0, len(nums) - 1)
        
    def subTree(self, start: int, end: int) -> TreeNode:
        if start  > end: return None
        if start == end: return TreeNode(self.nums[start])
        
        mid = (start + end) // 2
        
        node = TreeNode(self.nums[mid])
        node.left  = self.subTree(start, mid - 1)
        node.right = self.subTree(mid + 1, end)
        
        return node