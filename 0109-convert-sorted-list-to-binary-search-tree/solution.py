class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #: (base case)
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        # ==================================================
        #  Linked List + Tree + DFS + Recursion            =
        # ==================================================
        # time  : O(nlog(n))
        # space : O(log(n)) due to height-balanced BST
        
        def findMid(node) -> TreeNode:
            prevP, slowP, fastP = None, node, node
            
            while fastP and fastP.next:
                prevP = slowP
                slowP = slowP.next
                fastP = fastP.next.next
            
            #: DISCONNECT the left half from the mid node.
            if prevP: prevP.next = None
                
            return slowP
            
        mid  = findMid(head)
        
        node       = TreeNode(mid.val)
        node.left  = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node
    
    '''
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # (base case)
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        # ==================================================
        #  Linked List + Tree + In-order Recursion         =
        # ==================================================
        # time  : O(n)
        # space : O(log(n)) due to height-balanced BST
        
        cur, size = head, 0
        while cur:
            size += 1
            cur = cur.next
        
        self.head = head
        return self.inOrder(0, size - 1)
        
    def inOrder(self, start: int, end: int) -> TreeNode:
        if start > end: return None
        
        mid = (start + end) // 2
        
        left = self.inOrder(start, mid - 1)
        val = self.head.val
        self.head = self.head.next
        right = self.inOrder(mid + 1, end)
        
        node = TreeNode(val, left, right)
        
        return node
    '''