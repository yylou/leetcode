class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # ==================================================
        #  Linked List + Math                              =
        # ==================================================
        # time  : O(max(n, m))
        # space : O(1)

        ret = cur = ListNode(0)
        
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = carry + val1 + val2
            carry = total // 10
            total %= 10
            
            cur.next = ListNode(total)
            cur = cur.next
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        if carry: cur.next = ListNode(carry)
        return ret.next