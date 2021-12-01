class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # (base case)
        if not head.next and n == 1: return None

        # ==================================================
        #  Linked List + Two Pointer                       =
        # ==================================================
        # time  : O(n), one pass
        # space : O(1)

        slowP, fastP = head, head

        # move fast-pointer to keep the gap(n) apart from slow-pointer
        for i in range(n): fastP = fastP.next

        # n == length of the linked list
        if not fastP: return head.next

        # move fast-pointer to the end, maintaining the gap
        while fastP.next: slowP, fastP = slowP.next, fastP.next

        slowP.next = slowP.next.next
        return head

        '''
        # ==================================================
        #  Linked List + Hash Table                        =
        # ==================================================
        # time  : O(n), one pass
        # space : O(n)

        ret = head

        index = 0
        table = dict()
        while head:
            table[index] = head
            head = head.next
            index += 1

        if n == index: return ret.next

        # find the node before the one that needs to be removed
        node = table[index - n - 1]
        node.next = node.next.next

        return ret
        '''
