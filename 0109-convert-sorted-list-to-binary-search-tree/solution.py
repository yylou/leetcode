#:  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#:  Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        #:  (edge case)
        if not head: return None
        if not head.next: return TreeNode( head.val )


        #:  Solution (1) convery list to array at first
        #:  - time complexity: O(n)
        #:  - space complexity: O(n)
        array = []
        while head:
            array.append( head.val )
            head = head.next

        def subtree( left, right ):
            if left > right: return None
            if left == right: return TreeNode( array[left] )

            center = (left + right) // 2

            node = TreeNode( array[center] )
            node.left = subtree( left, center-1 )
            node.right = subtree( center+1, right)

            return node


        return subtree( 0, len(array)-1 )


        # ======================================================================= #


        #:  Solution (2) In-order Traversal Simulation
        #:  - time complexity: O(n)
        #:  - space complexity: O(logn) (due to recursive call)
        size = 0
        tmp = head
        while tmp:
            size += 1
            tmp = tmp.next

        global head_tmp
        head_tmp = head

        def simulation( left, right ):
            global head_tmp

            if left > right: return None

            center = (left + right ) // 2
            left = simulation( left, center-1 )

            node = TreeNode( head_tmp.val )
            node.left = left

            head_tmp = head_tmp.next
            node.right = simulation( center+1, right )

            return node


        return simulation( 0, size-1 )
