##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        cur   = ListNode()
        ret   = cur
        carry = 0

        while l1 != None or l2 != None :
            ##  Loop through l1 and l2
            if l1 != None : num1 = l1.val
            else : num1 = 0
            if l2 != None : num2 = l2.val
            else : num2 = 0

            ##  Calculation
            total = num1 + num2 + carry
            carry = total / 10
            cur.next = ListNode( total % 10 )
            cur = cur.next

            if l1 != None : l1 = l1.next
            if l2 != None : l2 = l2.next

        if carry != 0 : cur.next = ListNode( carry )
        return ret.next
