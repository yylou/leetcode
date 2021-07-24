class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # (base case)
        if not root: return 0
        if not root.children: return 1
        
        # ==================================================
        #  N-ary Tree + Level Order Traversal              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        maxDepth = 0
        stack = [root]
        
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                
                for element in node.children:
                    stack.append(element)
            
            maxDepth += 1
            
        return maxDepth