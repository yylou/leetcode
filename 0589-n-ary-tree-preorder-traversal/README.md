# Problem
[589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python
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

        retVal = [root.val]

        def recursive(node, retVal):
            retVal.append(node.val)

            if node.children:
                for childNode in node.children:
                    recursive( childNode, retVal )

        for node in root.children:
            recursive(node, retVal)

        return retVal
        '''
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    LinkedList<Integer> answer;
    
    public List<Integer> preorder(Node root) {
        answer = new LinkedList<Integer>();
        
        /* base case */
        if(root == null) return answer;
        
        answer.add(root.val);
        
        if(root.children == null) return answer;
        
        for(Node node: root.children) {
            recursive(node);
        }
        
        return answer;
    }
    
    public void recursive(Node root) {
        answer.add(root.val);
        
        if(root.children != null ) {
            for(Node node: root.children) {
                recursive(node);
            }
        }
    }
}
```