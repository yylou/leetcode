# Problem
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python
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
