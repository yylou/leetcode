class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # (base case)
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]

        # ==================================================
        #  Linked List + Sort                              =
        # ==================================================
        # time  : O(nlogk)
        # space : O(1)
        #
        # n is the total number of nodes in two linked lists
        # k is the number of linked lists

        size = 1
        while size < len(lists):
            for i in range(0, len(lists) - size, size * 2):
                lists[i] = self._merge(lists[i], lists[i+size])
            size *= 2

        return lists[0]

        """
                                        length = 6
            [l0, l1, l2, l3, l4, l5]    size = 1, interval = 2, upper = 5
             ^----^  ^----^  ^----^

            [l0,     l2,     l4    ]    size = 2, interval = 4, upper = 4
             ^--------^

            [l0,             l4    ]    size = 4, interval = 8, upper = 2
             ^----------------^

                                        length = 5
            [l0, l1, l2, l3, l4]        size = 1, interval = 2, upper = 5
             ^----^  ^----^

            [l0,     l2,     l4]        size = 2, interval = 4, upper = 4
             ^--------^

            [l0,             l4]        size = 4, interval = 8, upper = 2
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
