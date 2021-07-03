class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #  (base case)
        if not l1 and l2: return l2
        if not l2 and l1: return l1
        if not l1 and not l2: return None
        
        # ==================================================
        #  Linked List + Two Pointers                      =
        # ==================================================
        # n is the length of l1, and m is the length of l2
        # time  : O(n+m), 
        # space : O(1)
            
        ret = cur = ListNode(0)
        
        #  keep iterating both lists until either one meets the end
        #  append the one with SMALLER node and move it to the next
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                
            else:
                cur.next = l2
                l2 = l2.next
                
            cur = cur.next
            
        #  append the remaining linked lists, either l1 or l2
        cur.next = l1 or l2
            
        return ret.next
    
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n+m)
     * @space : O(1)
     */

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode(0);

        ListNode cur = ret;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                cur.next = l1;
                l1 = l1.next;
                
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            
            cur = cur.next;
        }

        cur.next = l1 == null ? l2 : l1;

        return ret.next;
    }
}
==================================================================================================
'''
