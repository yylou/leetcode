class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # (base case)
        if not root: return []
        if not root.children: return [root.val]
        
        # ==================================================
        #  N-ary Tree + Pre-order Traversal   (Iterative)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            if node.children:
                for i in range(len(node.children)-1, -1, -1):
                    stack.append(node.children[i])
                
        return ans
        
        '''
        # ==================================================
        #  N-ary Tree + Pre-order Traversal   (Recursive)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        
        def recursive(node: 'Node') -> None:
            ans.append(node.val)
            
            if node.children:
                for element in node.children:
                    recursive(element)
        
        recursive(root)
        return ans
        '''