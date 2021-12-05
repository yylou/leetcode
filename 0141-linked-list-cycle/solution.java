class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */

    public boolean hasCycle(ListNode head) {
        /* base case */
        if(head == null || head.next == null) return false;
        if(head.next.next == head) return true;

        ListNode slowP = head, fastP = head;

        while(fastP != null && fastP.next != null) {
            slowP = slowP.next;
            fastP = fastP.next.next;
            if(slowP == fastP) return true;
        }

        return false;
    }
}
