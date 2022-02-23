class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        #  (base case)
        if not head or not head.next: return head

        # ==================================================
        #  Linked List + Merge Sort           (Iterative)  =
        # ==================================================
        # time  : O(nlog(n))
        # space : O(1)

        length = self.getSize(head)
        ret, size = ListNode(0, head), 1

        while size < length:
            splitHead, mergeHead = ret.next, ret

            while splitHead:
                left  = splitHead
                right = self.split(size, left)
                splitHead = self.split(size, right)

                mergeHead = self.merge(left, right, mergeHead)

            size *= 2

        return ret.next

    def getSize(self, node: ListNode) -> int:
        size, tmp = 0, node
        while tmp: size, tmp = size + 1, tmp.next
        return size

    def split(self, size: int, node: ListNode) -> ListNode:
        pre, cur = None, node
        for i in range(size):
            if not cur: break
            pre, cur = cur, cur.next

        #  (break the link)
        if pre: pre.next = None
        return cur

    def merge(self, left: ListNode, right: ListNode, head: ListNode) -> ListNode:
        while left and right:
            if left.val <= right.val: head.next, left = left, left.next
            else: head.next, right = right, right.next

            head = head.next

        head.next = left if left else right
        while head.next: head = head.next
        return head

    '''
    def sortList(self, head: ListNode) -> ListNode:
        #  (base case)
        if not head or not head.next: return head

        # ==================================================
        #  Linked List + Merge Sort           (Recursive)  =
        # ==================================================
        # time  : O(nlog(n))
        # space : O(log(n))

        mid   = self.split(head)
        left  = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def split(self, node: ListNode) -> ListNode:
        if not node or not node.next: return head

        pre, slowP, fastP = node, node, node

        while fastP and fastP.next:
            pre   = slowP
            slowP = slowP.next
            fastP = fastP.next.next

        pre.next = None
        return slowP

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        ret = ListNode(0)
        head = ret

        while left and right:
            if left.val <= right.val:
                head.next = ListNode(left.val)
                left = left.next
            else:
                head.next = ListNode(right.val)
                right = right.next

            head = head.next

        head.next = left if (left and not right) else right

        return ret.next
    '''
