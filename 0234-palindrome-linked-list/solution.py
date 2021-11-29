class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # (base case) only one node
        if not head.next: return True

        # ==================================================
        #  In-place Reverse Half then Compare              =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        # Reverse first-half / Find middle
        rev, fast, slow = None, head, head
        while fast and fast.next:
            fast = fast.next.next

            tmp = rev
            rev = slow
            slow = slow.next
            rev.next = tmp

        # Skip middle point
        if fast: slow = slow.next

        # Compare
        while rev and slow:
            if rev.val != slow.val: return False
            rev, slow = rev.next, slow.next

        return True

        """
        N    1 -> 2 -> 3 -> 2 -> 1 -> N
             s
             f
        r

        N <- 1    2 -> 3 -> 2 -> 1 -> N
             r    s    f

        N <- 1 <- 2    3 -> 2 -> 1 -> N
                  r    s         f

        N <- 1 <- 2    3 -> 2 -> 1 -> N
                  r         s    f
        """

        """
        N    1 -> 2 -> 2 -> 1 -> N
             s
             f
        r

        N <- 1 <- 2    2 -> 1 -> N
                  r    s         f
        """

        """
        N    1 -> 2 -> N
             s
             f
        r

        N <- 1    2 -> N
             r    s    f
        """


        """
        # ==================================================
        #  Store each node's value                         =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        record = []
        while head:
            record.append( head.val )
            head = head.next

        return record == record[::-1]
        """
