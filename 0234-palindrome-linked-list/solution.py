class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # (base case)
        if not head.next: return True

        # ==================================================
        #  In-place Reverse Half then Compare              =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        # Reverse first-half / Find middle
        prev, fast, slow = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next

            slow.next = prev
            prev = slow

            slow = tmp

        # For odd length, fast stops at tail
        # For even length, fast stops at tail's next
        if fast: slow = slow.next

        # Compare
        while prev and slow:
            if prev.val != slow.val: return False
            prev, slow = prev.next, slow.next

        return True

        """
        N    1 -> 2 -> 3 -> 2 -> 1 -> N
             s
             f
        p

        N <- 1    2 -> 3 -> 2 -> 1 -> N
             p    s    f

        N <- 1 <- 2    3 -> 2 -> 1 -> N
                  p    s         f

        N <- 1 <- 2    3 -> 2 -> 1 -> N
                  p         s    f
        """

        """
        N    1 -> 2 -> 2 -> 1 -> N
             s
             f
        p

        N <- 1 <- 2    2 -> 1 -> N
                  p    s         f
        """

        """
        N    1 -> 2 -> N
             s
             f
        p

        N <- 1    2 -> N
             p    s    f
        """

        """
        # ==================================================
        #  Find middle with string record                  =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        stack = []
        # Find middle / Append elements
        prev, fast, slow = None, head, head
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        # For odd length, fast stops at tail
        # For even length, fast stops at tail's next
        if fast: slow = slow.next

        # Compare
        while slow:
            if slow.val != stack.pop(): return False
            slow = slow.next

        return True
        """
