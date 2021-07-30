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
    
    '''
    class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        # ==================================================
        #  Linked List                        (Recursive)  =
        # ==================================================
        # time  : O(m+n)
        # space : O(max(m,n)
    
        len1, len2 = self.length(l1), self.length(l2)
        
        if len1 > len2: l2 = self.fill(l2, len1 - len2)
        elif len2 > len1: l1 = self.fill(l1, len2 - len1)
        
        carry, ret = self.merge(l1, l2)
        
        if carry: ret = ListNode(1, ret)
        return ret
        
    def length(self, l: ListNode) -> int:
        length, tmp = 0, l
        while tmp:
            length += 1
            tmp = tmp.next
        return length
    
    def fill(self, l: ListNode, num: int) -> ListNode:
        ret = head = ListNode(-1)
        for i in range(num):
            head.next = ListNode(0)
            head = head.next
        head.next = l
        return ret.next

    #
    # Recursive to merge two lists while summing nodes' values
    #
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return (0, None)
        carry, next = self.merge(l1.next, l2.next)
        curSum = l1.val + l2.val + carry
        node = ListNode(curSum % 10, next)
        return (curSum // 10, node)
    '''