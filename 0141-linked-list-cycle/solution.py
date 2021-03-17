##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        ##  (edge case) head is null / head has no next node
        if not head or not head.next: return False

        ##  (1) visit each node and modify the next node to tmpNode
        ##  (2) if certain node's next is tmpNode, there is a cycle
        tmpNode = ListNode( -1 )
        while head:
            if head.next == None: return False
            if head.next == tmpNode: return True

            nextNode = head.next
            head.next = tmpNode
            head = nextNode
