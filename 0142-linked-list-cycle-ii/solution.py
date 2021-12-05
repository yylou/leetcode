class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # (base case)
        if not head or not head.next: return None
        if head == head.next.next: return head

        # ==================================================
        #  Linked List + Two Pointer (Floyd's algorithm)   =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        slowP, fastP = head, head

        # Find the intersection
        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP == fastP: break

        if slowP != fastP: return None

        # Find the cycle entrance
        slowP = head
        while slowP != fastP:
            slowP = slowP.next
            fastP = fastP.next

        return slowP
