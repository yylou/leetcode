class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # (base case)
        if not root.left and not root.right: return True
        
        # ==================================================
        #  Tree                               (Iterative)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            
            # no child nodes, continue instead of pushing null nodes
            if not (node1  or node2): continue
                
            if not (node1 and node2): return False
            if node1.val != node2.val: return False
            
            stack.append((node1.left,  node2.right))
            stack.append((node1.right, node2.left))
            
        return True