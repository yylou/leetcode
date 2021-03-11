##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        ##  RECORD all the values in all linked lists
        valList = []
        for element in lists:
            while element:
                valList.append( element.val )
                element = element.next

        ##  SORT (time complexity: O(nlogn))
        valList.sort()

        ##  Loop through sorted list to build linked list
        head = ListNode()
        retNode = head

        for val in valList:
            node = ListNode( val )
            head.next = node
            head = node

        return retNode.next
