# Problem
[141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Proof of Floyd Cycle Chasing (Tortoise and Hare)
```
The distance from the head (inclusive) to the joint (exclusive) is F.
The distance from the joint (inclusive) to the meet point (exclusive) is a.
The distance from the meet point (inclusice) to the joint (exclusive) is C-a.

At meet point, support hare has run n cycles.
2(F + a) = F + nC + a, F + a = nC

We further assign hare to the head and make their speed be the same.
After F steps, hare is at F and turtle is at (nC + F) mod C = F, we find the intersection point.
```

# Python
```Python3
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # (base case)
        if not head or not head.next: return False
        if head.next.next == head: return True
        
        # ==================================================
        #  Linked List + Two Pointer                       =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        slowP, fastP = head, head
        
        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP == fastP: return True
        
        return False
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
     
    public boolean hasCycle(ListNode head) {
        /* base case */
        if(head == null || head.next == null) return false;
        if(head.next.next == head) return true;
        
        ListNode slowP = head, fastP = head;
        
        while(fastP != null && fastP.next != null) {
            slowP = slowP.next;
            fastP = fastP.next.next;
            if(slowP == fastP) return true;
        }
        
        return false;
    }
}
```
