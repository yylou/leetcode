##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        ##  (edge case) linked list only has one node
        if not head.next: return True


        ##  Solution (1) reverse half (in-place) and then compare
        ##  (a) find the half-point (NOTE: BEFORE the real half-point)
        fastP, slowP = head, head
        while fastP.next and fastP.next.next:
            fastP = fastP.next.next
            slowP = slowP.next

        halfNode = slowP.next

        ##  (b) reverse the second-half of linked list (NOTE: take the PREV NODE)
        preNode, curNode = None, halfNode
        while curNode:
            nexNode = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = nexNode

        newHead = preNode

        ##  (c) compare
        while head and newHead:
            if head.val != newHead.val: return False
            head = head.next
            newHead = newHead.next

        return True


        # =================================================================== #


        ##  Solution (2) record each node's value with space complexity O(n)
        record = []
        while head:
            record.append( head.val )
            head = head.next

        return record == record[::-1]
