# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur   = ListNode()
        ret   = cur
        carry = 0
        
        # ==================================================
        #  Linked List + Math                              =
        # ==================================================
        # time  : O(max(n, m))
        # space : O(1)
        
        while l1 or l2:
            if l1: num1 = l1.val
            else: num1 = 0
                
            if l2: num2 = l2.val
            else: num2 = 0
            
            tmp      = num1 + num2 + carry
            carry    = tmp // 10
            cur.next = ListNode( tmp % 10 )
            cur      = cur.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        #:  check carry to see whether creating extra node is needed
        if carry != 0: cur.next = ListNode( carry )
            
        return ret.next
    
    
    
'''
Java Solution
==================================================================================================
class Solution {
    /**  
     * @time  : O(max(n, m))
     * @space : O(1)
     */
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
    }
}
==================================================================================================
'''
