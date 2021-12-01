class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # (base case)
        if not l2 and l1: return l1
        if not l1 and l2: return l2
        if not l1 and not l2: return None

        # ==================================================
        #  Linked List + Recursion                         =
        # ==================================================
        # n is the length of l1, and m is the length of l2
        # time  : O(n+m)
        # space : O(n+m)

        if l1.val > l2.val: l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

        '''
        # ==================================================
        #  Linked List + Two Pointers                      =
        # ==================================================
        # n is the length of l1, and m is the length of l2
        # time  : O(n+m)
        # space : O(1)

        ret = cur = ListNode(0)

        # Keep iterating both lists until either one meets the end
        # Append the one with SMALLER node and move it to the next
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        # Append the remaining linked lists, either l1 or l2
        cur.next = l1 or l2

        return ret.next
        '''
