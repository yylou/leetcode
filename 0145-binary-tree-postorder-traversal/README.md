# Problem
[145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # (base case)
        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        # ==================================================
        #  Binary Tree + Post-order Traversal              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ans = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    
        return ans
    
        '''
        # ==================================================
        #  Binary Tree + Post-order Traversal              =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        '''
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    
    public List<Integer> postorderTraversal(TreeNode root) {
        /* base case */
        if(root == null) return new ArrayList<>();
        
        List<Integer> result = new ArrayList<>();
        Stack<Pair<TreeNode, Boolean>> stack = new Stack<Pair<TreeNode, Boolean>>();
        stack.push(new Pair<TreeNode, Boolean>(root, false));
        
        while(!stack.isEmpty()) {
            Pair<TreeNode, Boolean> object = stack.pop();
            TreeNode node = object.getKey();
            Boolean visited = object.getValue();
            
            if(visited == true) result.add(node.val);
            else {
                stack.push(new Pair<TreeNode, Boolean>(node, true));
                if(node.right != null) stack.push(new Pair<TreeNode, Boolean>(node.right, false));
                if(node.left != null) stack.push(new Pair<TreeNode, Boolean>(node.left, false));
            }
        }
        
        return result;
    }
}
```