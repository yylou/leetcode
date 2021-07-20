class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public ListNode reverseList(ListNode head) {
        if( head == null || head.next == null ) return head;
        
        ListNode prev = null;
        while( head != null ){
            ListNode tmp = head.next;
            head.next = prev;
            prev = head;
            head = tmp;
        }
        return prev;
    }
}
