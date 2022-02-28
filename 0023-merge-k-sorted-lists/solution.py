class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # (base case)
        if not lists: return None
        if len(lists) == 1: return lists[0]

        # ==================================================
        #  Linked List + Sort                              =
        # ==================================================
        # time  : O(nlogk)
        # space : O(1)
        #
        # n is the total number of nodes in two linked lists
        # k is the number of linked lists

        length = len(lists)
        size = 1
        while size < length:
            for i in range(0, length, size * 2):
                if i + size < length: lists[i] = self._merge(lists[i], lists[i + size])
            size *= 2

        return lists[0]

        """
                                        length = 6
            [l0, l1, l2, l3, l4, l5]    size = 1, interval = 2
             ^----^  ^----^  ^----^

            [l0,     l2,     l4    ]    size = 2, interval = 4
             ^--------^

            [l0,             l4    ]    size = 4, interval = 8
             ^----------------^

                                        length = 5
            [l0, l1, l2, l3, l4]        size = 1, interval = 2
             ^----^  ^----^

            [l0,     l2,     l4]        size = 2, interval = 4
             ^--------^

            [l0,             l4]        size = 4, interval = 8
             ^----------------^
        """

    def _merge(self, l1, l2):
        head = cur = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val: cur.next, l1 = l1, l1.next
            else: cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 or l2
        return head.next
