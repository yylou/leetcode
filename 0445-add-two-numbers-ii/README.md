# Problem
[445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python3
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
```

# Java
```Java
class Solution {
    /**
     * @time  : O(m+n)
     * @space : O(m+n)
     */
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> stack1 = new Stack<Integer>();
        Stack<Integer> stack2 = new Stack<Integer>();
        
        while(l1 != null) {
            stack1.push(l1.val);
            l1 = l1.next;
        };
        while(l2 != null) {
            stack2.push(l2.val);
            l2 = l2.next;
        }
        
        int carry = 0;
        ListNode ret = null;
        while (!stack1.empty() || !stack2.empty() || carry != 0) {
            int val1 = (!stack1.empty()) ? stack1.pop() : 0;
            int val2 = (!stack2.empty()) ? stack2.pop() : 0;
            int curSum = val1 + val2 + carry;
            carry = curSum / 10;
            curSum = curSum % 10;
            ret = new ListNode(curSum, ret);
        }
        
        return ret;
    }
}
```
