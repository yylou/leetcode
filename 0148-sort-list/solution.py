#:  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #:  Solution (1) using List to record
        #:  - time complexity: O(n)
        #:  - space complexity: O(n)

        #:  (edge case)
        if not head or not head.next: return head

        valList = []

        tmpNode = head
        while tmpNode:
            valList.append( tmpNode.val )
            tmpNode = tmpNode.next

        valList.sort()

        tmpNode = head
        for element in valList:
            tmpNode.val = element
            tmpNode = tmpNode.next

        return head


        # ========================================================================== #


        #:  Solution (2) Top-down Merge Sort
        #:  - time complexity: O(nlogn)
        #:  - space complexity: O(logn)

        def getMid(node):
            slowP, fastP = node, node
            while fastP.next and fastP.next.next:
                slowP = slowP.next
                fastP = fastP.next.next

            fastP = slowP.next
            slowP.next = None
            return fastP

        def merge(l1, l2):
            if not l1 and not l2: return None
            if l1 and not l2: return l1
            if not l1 and l2: return l2

            if l1.val > l2.val:
                golden = l2
                refer = l1
            else:
                golden = l1
                refer = l2

            head = golden

            while refer:
                if not golden.next:
                    golden.next = refer
                    return head

                elif refer.val >= golden.val and refer.val < golden.next.val:
                    golden.next = ListNode( refer.val, golden.next )
                    refer = refer.next

                else:
                    golden = golden.next

            return head

        #:  (edge case)
        if not head or not head.next: return head

        mid   = getMid( head )
        left  = self.sortList( head )
        right = self.sortList( mid )

        return merge( left, right )


        # ========================================================================== #


        #:  Solution (3) Bottom-up Merge Sort
        #:  - time complexity: O(nlogn)
        #:  - space complexity: O(1)

        def getSize( head ):
            size = 0
            while head:
                size += 1
                head = head.next

            return size

        def split( head, size ):
            for i in xrange( size-1 ):
                if not head: break
                head = head.next

            if not head: return None

            nextNode, head.next = head.next, None
            return nextNode

        def merge( l1, l2, start ):
            curNode = start
            while l1 and l2:
                if l1.val <= l2.val:
                    curNode.next, l1 = l1, l1.next
                else:
                    curNode.next, l2 = l2, l2.next

                curNode = curNode.next

            curNode.next = l1 if l1 else l2
            while curNode.next: curNode = curNode.next

            return curNode

        #:  (edge case)
        if not head or not head.next: return head

        #:  Get total length
        length = getSize( head )

        dummyNode = ListNode( 0 )
        dummyNode.next = head

        start, dummyStart, size = None, None, 1

        while size < length:
            #:  re-Initialize
            dummyStart = dummyNode
            start = dummyNode.next

            #:  SPLIT and MERGE-SORT
            while start:
                left = start
                right = split( left, size )
                start = split( right, size )

                dummyStart = merge( left, right, dummyStart )

            size *= 2

        return dummyNode.next
