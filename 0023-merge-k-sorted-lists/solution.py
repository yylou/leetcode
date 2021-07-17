class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # (base case)
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        
        # ==================================================
        #  Linked List + Sort                              =
        # ==================================================
        # time  : O(nlogk)
        # space : O(1)
        # 
        # n is the total number of nodes in two linked lists
        # k is the number of linked lists
        
        size = 1
        while size < len(lists):
            for i in range(0, len(lists) - size, size * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i+size])
            size *= 2
            
        return lists[0]
        
    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        cur = ret
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
                
        cur.next = l1 or l2
                
        return ret.next
