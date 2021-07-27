# Problem
[109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # (base case)
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        # ==================================================
        #  Linked List + Tree + DFS + Recursion            =
        # ==================================================
        # time  : O(nlog(n))
        # space : O(log(n)) due to height-balanced BST
        
        mid = self.findMid(head)
        
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node
        
    def findMid(self, node: ListNode) -> TreeNode:
        pre, slow, fast = None, node, node
        while fast and fast.next:
            pre  = slow
            slow = slow.next
            fast = fast.next.next
            
        # DISCONNECT the left half from the mid node.
        if pre: pre.next = None
            
        return slow
```

```python
class Solution:
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
        node = TreeNode(self.head.val)
        node.left = left
        self.head = self.head.next
        
        node.right = self.inOrder(mid + 1, end)
        
        return node
```

# Java
```Java
class Solution {
    /**
     * @time  : O(nlog(n))
     * @space : O(log(n)) due to height-balanced BST
     */
     
    public ListNode findMid(ListNode head) {
        ListNode prevP = null, slowP = head, fastP = head;
        
        while(fastP != null && fastP.next != null) {
            prevP = slowP;
            slowP = slowP.next;
            fastP = fastP.next.next;
        }
        
        if(prevP != null) prevP.next = null;
        return slowP;
    }
    
    public TreeNode sortedListToBST(ListNode head) {
        /* base case */
        if(head == null) return null;
        if(head.next == null) return new TreeNode(head.val);
        
        ListNode mid = findMid(head);
        
        TreeNode node = new TreeNode(mid.val);
        node.left     = sortedListToBST(head);
        node.right    = sortedListToBST(mid.next);
        
        return node;
    }
}
```
