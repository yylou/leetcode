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
            if l1: 
                num1 = l1.val
                l1 = l1.next
            else: 
                num1 = 0
                
            if l2: 
                num2 = l2.val
                l2 = l2.next
            else: 
                num2 = 0
            
            val      = num1 + num2 + carry
            carry    = val // 10
            cur.next = ListNode(val % 10)
            cur      = cur.next
        
        # check carry to see if need to create extra node
        if carry != 0: cur.next = ListNode(carry)
            
        return ret.next
