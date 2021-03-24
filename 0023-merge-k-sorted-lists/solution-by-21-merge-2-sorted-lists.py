##  Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    # =====================================================
    #  LeetCode 23. Merge k Sorted Lists                  =
    # =====================================================
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        length = len( lists )
        
        ##  (edge case) lists is empty or only has 1 element
        if not lists: return None
        if length == 1: return lists[0]
        
        
        ##  Solution (1) merge two lists in each iteration, time compliexity: O(nlogk)
        jump = 1
        while jump < length:
            for i in xrange( 0, length-jump, jump*2 ):
                lists[i] = self.mergeTwoLists( lists[i], lists[i+jump] )
            jump *= 2
        return lists[0]
        
        
        ##  Solution (2) merge list one-by-one, time complexity: O(nk)
        merged = lists[0]
        for i in range( 1, length ): merged = self.mergeTwoLists( merged, lists[i] )
        return merged
    

    # =====================================================
    #  LeetCode 21. Merge Two Sorted Lists                =
    # =====================================================
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ##  (edge case)
        if not l1 and not l2 : return None
        if not l1 and     l2 : return l2
        if     l1 and not l2 : return l1
        
        ##  compare the first element to choose the SMALLER one to be the GOLDEN (headNode)
        if l1.val > l2.val : 
            curNode_1 = l2
            curNode_2 = l1
            
        else : 
            curNode_1 = l1
            curNode_2 = l2

        headNode = curNode_1
        
        ##  loop through the non-GOLDEN linked list to do node insertion
        while curNode_2 :
            ##  reaching the end of GOLDEN linked list, append the rest and return
            if curNode_1.next == None : 
                curNode_1.next = curNode_2
                return headNode
                
            ##  do numerical comparison and insert the node
            elif curNode_2.val >= curNode_1.val and curNode_2.val < curNode_1.next.val : 
                curNode_1.next = ListNode( curNode_2.val, curNode_1.next )
                curNode_2 = curNode_2.next
            
            ##  the value of target node is smaller, move to the next node of GOLDEN list
            else : 
                curNode_1 = curNode_1.next
                
        return headNode
