# Problem
[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python3
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #  (base case)
        if not head.next and n == 1: return None
        
        # ==================================================
        #  Linked List + Two Pointer                       =
        # ==================================================
        # time  : O(n), one pass
        # space : O(1)
        
        slowP, fastP = head, head
        
        for i in range(n): fastP = fastP.next
        
        #  move fast-pointer to keep the gap(n) apart from slow-pointer
        if not fastP:
            head = head.next
            return head
        
        while fastP.next:
            slowP = slowP.next
            fastP = fastP.next
            
        slowP.next = slowP.next.next
        return head
```

```Python3
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #  (base case)
        if not head.next and n == 1: return None
        
        # ==================================================
        #  Linked List + Hash Table                        =
        # ==================================================
        # time  : O(n), one pass
        # space : O(n)
        
        ret = head
        
        counter = 0
        table = dict()
        while head:
            table[counter] = head
            head = head.next
            counter += 1
        
        if n == counter: return ret.next
        
        node = table[counter - n - 1]
        node.next = node.next.next
        
        return ret
```

# Java
```Java
class Solution {
    /**  
     * @time  : O(n)
     * @space : O(1)
     */
    
    public ListNode removeNthFromEnd(ListNode head, int n) {
        /* base case */
        if(head.next == null && n == 1) return null;
        
        ListNode slowP = head, fastP = head;
        
        /* Advances fast-pointer so that the gap between two pointers is n nodes apart */
        for (int i=0 ; i<n ; i++) fastP = fastP.next;
        
        /* nth node from the end points to HEAD */
        if(fastP == null) {
            head = head.next;
            return head;
        }
            
        /* Move fast-pointer to the end, maintaining the gap */
        while (fastP.next != null) {
            slowP = slowP.next;
            fastP = fastP.next;
        }
        
        slowP.next = slowP.next.next;
        return head;
    }
}
```
