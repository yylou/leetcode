##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##  iterative solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ##  (edge case) null node or single node
        if head      == None : return head
        if head.next == None : return head

        preNode = None
        curNode = head

        while curNode is not None :
            tmpNode = curNode.next

            ##  SWAP / REVERSE link
            curNode.next = preNode
            preNode = curNode

            ##  move forward the current node
            curNode = tmpNode

        return preNode
