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
