class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # (base case)
        if not root: return []
        if not root.children: return [root.val]
        
        # ==================================================
        #  N-ary Tree + Post-order Traversal  (Iterative)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if visited: ans.append(node.val)
                
            else:
                stack.append((node, True))
                
                for i in range(len(node.children)-1, -1, -1):
                    stack.append((node.children[i], False))
                        
        return ans

        '''
        # ==================================================
        #  N-ary Tree + Post-order Traversal  (Recursive)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        global ans
        ans = []
        
        def recursive(node) -> None:
            if node.children:
                for element in node.children:
                    recursive(element)
            
            ans.append(node.val)
        
        recursive(root)
        return ans
        '''
