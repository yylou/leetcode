class Solution {
    /**  
     * @time  : O(n)
     * @space : O(1)
     */
    
    public ListNode removeNthFromEnd(ListNode head, int n) {
        /* base case */
        if(head.next == null && n == 1) return null;
        
        ListNode slowP = head, fastP = head;
        
        /* Move fast-pointer so that the gap between two pointers is n nodes apart */
        for (int i=0 ; i<n ; i++) fastP = fastP.next;
        
        /* nth node from the end points to HEAD */
        if(fastP == null) return head.next;
            
        /* Move fast-pointer to the end, maintaining the gap */
        while (fastP.next != null) {
            slowP = slowP.next;
            fastP = fastP.next;
        }
        
        slowP.next = slowP.next.next;
        return head;
    }
}