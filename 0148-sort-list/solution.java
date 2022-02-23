class Solution {
    /**
     * @time  : O(nlog(n))
     * @space : O(1)
     */

    public ListNode sortList(ListNode head) {
        /* base case */
        if(head == null || head.next == null) return head;

        int len = getLen(head);

        int size = 1;
        ListNode ret = new ListNode(0, head);

        while(size < len) {
            ListNode splitHead = ret.next, mergeHead = ret;
            while(splitHead != null) {
                ListNode left  = splitHead;
                ListNode right = split(size, left);
                splitHead = split(size, right);

                mergeHead = merge(left, right, mergeHead);
            }

            size *= 2;
        }

        return ret.next;
    }

    public int getLen(ListNode head) {
        int len = 0;
        ListNode cur = head;
        while(cur != null) {
            len++;
            cur = cur.next;
        }
        return len;
    }

    public ListNode split(int size, ListNode node) {
        ListNode pre = null;
        for(int i=0 ; i<size ; i++) {
            if(node == null) break;
            pre = node;
            node = node.next;
        }
        /* break the link */
        if(pre != null) pre.next = null;
        return node;
    }

    public ListNode merge(ListNode left, ListNode right, ListNode head) {
        while(left != null && right != null) {
            if(left.val <= right.val) {
                head.next = left;
                left = left.next;
            } else {
                head.next = right;
                right = right.next;
            }
            head = head.next;
        }
        head.next = (left != null) ? left : right;
        while(head.next != null) head = head.next;
        return head;
    }
}
