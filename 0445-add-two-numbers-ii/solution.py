class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        # ==================================================
        #  Linked List + Stack                             =
        # ==================================================
        # time  : O(m+n)
        # space : O(m+n)
    
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry, ret = 0, None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            curSum = val1 + val2 + carry
            carry = curSum // 10
            curSum = curSum % 10
            
            ret = ListNode(curSum, ret)
        
        return ret