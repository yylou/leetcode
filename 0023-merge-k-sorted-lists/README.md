# Problem
[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python3
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # (base case)
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        
        # ==================================================
        #  Linked List + Sort                              =
        # ==================================================
        # time  : O(nlogk)
        # space : O(1)
        # 
        # n is the total number of nodes in two linked lists
        # k is the number of linked lists
        
        size = 1
        while size < len(lists):
            for i in range(0, len(lists) - size, size * 2):
                lists[i] = self._merge(lists[i], lists[i+size])
            size *= 2
            
        return lists[0]

    def _merge(self, l1, l2):
        head = cur = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val: cur.next, l1 = l1, l1.next
            else: cur.next, l2 = l2, l2.next
            cur = cur.next
        
        cur.next = l1 or l2
        return head.next
```

# Java
```Java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        /* base case */
        if(lists.length == 0) return null;
        if(lists.length == 1) return lists[0];
        
        int size = 1;
        while(size < lists.length) {
            for(int i=0 ; i<lists.length-size ; i+=size*2) {
                lists[i] = merge2Lists(lists[i], lists[i+size]);
            }
            size *= 2;
        }
        return lists[0];
    }
    
    public ListNode merge2Lists(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode(0);
        ListNode cur = ret;
        
        while(l1 != null && l2 != null) {
            if(l1.val < l2.val) {
                cur.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                cur.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            cur = cur.next;
        }
        
        cur.next = (l2 == null) ? l1 : l2;
        
        return ret.next;
    }
}
```
