class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # (base case)
        if not p and not q: return True
        if not p or  not q: return False
        if p.val != q.val: return False
        
        # ==================================================
        #  Tree + DFS                         (Iterative)  =
        # ==================================================
        # time  : O(n)
        # space : O(n) for worst case, O(log(n)) for avg case
        
        stack = [(p,q)]
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2: continue
            
            if (node1 and not node2) or (not node1 and node2): return False
            if (node1 and node2) and node1.val != node2.val: return False
            
            stack.append((node1.left,  node2.left))
            stack.append((node1.right, node2.right))
            
        return True
    
        '''
        # ==================================================
        #  Tree + DFS                         (Recursive)  =
        # ==================================================
        # time  : O(n)
        # space : O(n) for worst case, O(log(n)) for avg case
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        '''