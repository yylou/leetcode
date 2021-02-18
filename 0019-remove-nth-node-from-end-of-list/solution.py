##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##  two-pointer solution: using the gap between two pointers to find the target node
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        ##  edge case handling
        if head.next == None : return None

        dummy_head = ListNode( -1 )
        dummy_head.next = head

        flag_node, cur_node = dummy_head, dummy_head

        while n:
            flag_node = flag_node.next
            n -= 1

        while flag_node.next:
            flag_node = flag_node.next
            cur_node = cur_node.next

        cur_node.next = cur_node.next.next

        return dummy_head.next
