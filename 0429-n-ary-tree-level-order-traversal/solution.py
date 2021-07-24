class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # (base case)
        if not root: return []
        if not root.children: return [[root.val]]
        
        # ==================================================
        #  N-ary Tree + Level Order Traversal (Iterative)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        stack = [root]
        
        while stack:
            tmp = []
            for i in range(len(stack)):
                node = stack.pop(0)
                tmp.append(node.val)
                
                for element in node.children: stack.append(element)
                    
            ans.append(tmp)
                    
        return ans

        '''
        # ==================================================
        #  N-ary Tree + Level Order Traversal (Recursive)  =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        
        def recursive(node: 'Node', level: int) -> None:
            if len(ans) == level: ans.append([])
                
            ans[level].append(node.val)
            
            if node.children:
                for element in node.children:
                    recursive(element, level + 1)
        
        recursive(root, 0)
        return ans
        '''