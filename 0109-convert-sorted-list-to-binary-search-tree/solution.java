class Solution {
    /**
     * @time  : O(nlog(n))
     * @space : O(log(n)) due to height-balanced BST
     */

    public ListNode findMid(ListNode head) {
        ListNode prevP = null, slowP = head, fastP = head;
        
        while(fastP != null && fastP.next != null) {
            prevP = slowP;
            slowP = slowP.next;
            fastP = fastP.next.next;
        }
        
        if(prevP != null) prevP.next = null;
        return slowP;
    }
    
    public TreeNode sortedListToBST(ListNode head) {
        /* base case */
        if(head == null) return null;
        if(head.next == null) return new TreeNode(head.val);
        
        ListNode mid = findMid(head);
        
        TreeNode node = new TreeNode(mid.val);
        node.left     = sortedListToBST(head);
        node.right    = sortedListToBST(mid.next);
        
        return node;
    }
}