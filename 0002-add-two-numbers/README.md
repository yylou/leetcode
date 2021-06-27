# Problem
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python
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
```
    
# Java
```Java
class Solution {
    /**  
     * @time  : O(max(n, m))
     * @space : O(1)
     */
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur = new ListNode();
        ListNode ret = cur;
        int carry = 0;
        
        while(l1 != null || l2 != null) {
            int num1, num2;
            
            if(l1 != null) num1 = l1.val;
            else num1 = 0;
            
            if(l2 != null) num2 = l2.val;
            else num2 = 0;
            
            int sum = num1 + num2 + carry;
            carry = sum / 10;
            sum = sum % 10;
            
            cur.next = new ListNode(sum);
            cur = cur.next;
            
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }
        
        if(carry != 0) cur.next = new ListNode(carry);
        return ret.next;
    }
}
```
