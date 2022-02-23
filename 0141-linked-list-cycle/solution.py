class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # (base case)
        if not head or not head.next: return False
        if head.next == head: return True

        # ==================================================
        #  Linked List + Two Pointer                       =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        slowP, fastP = head, head

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP == fastP: return True

        return False
