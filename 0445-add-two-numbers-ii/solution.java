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