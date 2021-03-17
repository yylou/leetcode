##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ##  (edge case) root is null / root has no next node
        if not head: return None
        if not head.next: return None


        ##  Solution (1) Floyd's algorithm
        ##  - time complexity: O(n)
        ##  - space complexity: O(1)
        slowP, fastP = head, head

        ##  (1) find the intersection
        while True:
            ##  reach the end, RETURN
            if slowP == None: return None
            if fastP == None or fastP.next == None: return None

            slowP = slowP.next
            fastP = fastP.next.next

            if slowP == fastP: break

        ##  (2) find the entrance of the cycle
        slowP = head
        while slowP != fastP:
            slowP = slowP.next
            fastP = fastP.next

        return slowP


        # ============================================================ #


        ##  Solution (2) using set to record the existing node
        ##  - time complexity: O(n)
        ##  - space complexity: O(n)
        record = set()
        while head is not None:
            if head in record: return head
            record.add( head )

            head = head.next

        return None
