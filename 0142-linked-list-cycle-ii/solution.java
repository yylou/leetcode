class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    
    public ListNode detectCycle(ListNode head) {
        /* case case */
        if(head == null || head.next == null) return null;
        if(head == head.next.next) return head;
        
        ListNode slowP = head, fastP = head;
        while(fastP != null && fastP.next != null) {
            slowP = slowP.next;
            fastP = fastP.next.next;
            if(slowP == fastP) break;
        }
        
        if(slowP != fastP) return null;
        
        slowP = head;
        while(slowP != fastP) {
            slowP = slowP.next;
            fastP = fastP.next;
        }
        
        return slowP;
    }
}
