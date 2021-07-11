class Solution {
    /**
     * @time  : O(n+m)
     * @space : O(n+m)
     */
  
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        /* base case */
        if(l1 != null && l2 == null) return l1;
        if(l1 == null && l2 != null) return l2;
        if(l1 == null && l2 == null) return null;

        if(l2.val < l1.val) {
            ListNode tmp = l1;
            l1 = l2;
            l2 = tmp;
        }
        l1.next = mergeTwoLists(l1.next, l2);
        
        return l1;
    }
}
