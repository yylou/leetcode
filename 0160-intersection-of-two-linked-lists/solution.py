##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        #:  (edge case)
        if (headA and not headB) or (not headA and headB) or (not headA and not headB): return None


        #:  Solution (1) a + shared + b == b + shared + a
        #:  - time complexity: O(n + m)
        #:  - space complexity: O(1)
        pA, pB = headA, headB
        while pA != pB:
            if not pA: pA = headB
            else: pA = pA.next

            if not pB: pB = headA
            else: pB = pB.next

        return pA


        # ============================================================================================= #


        ##  Solution (2) find the length of two lists and align before traversing
        #:  - time complexity: O(n + m)
        #:  - space complexity: O(1)
        lenA, lenB = 1, 1
        tmpA, tmpB = headA, headB
        while tmpA:
            lenA += 1
            tmpA = tmpA.next
        while tmpB:
            lenB += 1
            tmpB = tmpB.next

        if lenA > lenB:
            counter = lenA - lenB
            while counter:
                headA = headA.next
                counter -= 1
        else:
            counter = lenB - lenA
            while counter:
                headB = headB.next
                counter -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


        # ============================================================================================= #


        #:  Solution (3) using SET to record
        #:  - time complexity: O(n + m)
        #:  - space complexity: O(n)
        recA = set()
        while headA:
            recA.add(headA)
            headA = headA.next
        while headB:
            if headB in recA: return headB
            headB = headB.next

        return None
