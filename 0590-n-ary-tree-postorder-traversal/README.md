# Problem
[590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python
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

```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    LinkedList<Integer> ans;
    
    public List<Integer> postorder(Node root) {
        ans = new LinkedList<Integer>();
        
        /* base case */
        if(root == null) return ans;
        
        recursive(root);
        return ans;
    }
    
    public void recursive(Node root) {
        if(root.children != null ){
            for(Node node: root.children) {
                recursive(node);
            }
        }
        
        ans.add(root.val);
    }
}
```