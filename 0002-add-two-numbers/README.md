# Problem
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python
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
            
            if(l1 != null) {
                num1 = l1.val;
                l1 = l1.next;
            } else num1 = 0;
            
            if(l2 != null) {
                num2 = l2.val;
                l2 = l2.next;
            } else num2 = 0;
            
            int sum = num1 + num2 + carry;
            carry = sum / 10;
            sum = sum % 10;
            
            cur.next = new ListNode(sum);
            cur = cur.next;
        }
        
        if(carry != 0) cur.next = new ListNode(carry);
        return ret.next;
    }
}

```
