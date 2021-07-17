class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        /* base case */
        if(lists.length == 0) return null;
        if(lists.length == 1) return lists[0];
        
        int size = 1;
        while(size < lists.length) {
            for(int i=0 ; i<lists.length-size ; i+=size*2) {
                lists[i] = merge2Lists(lists[i], lists[i+size]);
            }
            size *= 2;
        }
        return lists[0];
    }
    
    public ListNode merge2Lists(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode(0);
        ListNode cur = ret;
        
        while(l1 != null && l2 != null) {
            if(l1.val < l2.val) {
                cur.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                cur.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            cur = cur.next;
        }
        
        cur.next = (l2 == null) ? l1 : l2;
        
        return ret.next;
    }
}
