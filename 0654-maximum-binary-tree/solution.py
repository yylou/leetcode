class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # (base case)
        if not nums: return None
        if len(nums) == 1: return TreeNode(nums[0])

        # ==================================================
        #  Binary Tree + Monotonic Stack                   =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        stack = []
        for num in nums:
            node, last = TreeNode(num), None

            # 1. (current node's value > previous node's value) pop from stack
            # 2. append the MAX element in the stack to current node's left
            while stack and stack[-1].val < num:
                last = stack.pop()
            node.left = last

            # (current node's value < previous node's value)
            # append current node to previous node's right
            if stack: stack[-1].right = node

            stack.append(node)

        return stack[0]

    '''
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # (base case)
        if not nums: return None
        if len(nums) == 1: return TreeNode(nums[0])

        # ==================================================
        #  Binary Tree + Recursion                         =
        # ==================================================
        # time  : O(n^2)
        # space : O(n)

        self.nums = nums
        return self.construct(0, len(nums))

    def construct(self, left: int, right: int) -> TreeNode:
        if left >= right: return None

        maxIndex = self.findMax(left, right)
        return TreeNode(self.nums[maxIndex], self.construct(left, maxIndex), self.construct(maxIndex + 1, right))

    def findMax(self, left: int, right: int) -> int:
        maxIndex = left
        for i in range(left, right):
            if self.nums[i] > self.nums[maxIndex]:
                maxIndex = i

        return maxIndex
    '''
