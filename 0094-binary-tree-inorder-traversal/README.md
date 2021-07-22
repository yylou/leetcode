# Problem
[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # (base case)
        if not root: return []
        if not root.left and not root.right: return [root.val]
        
        # ==================================================
        #  Binary Tree + In-order Traversal               =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        ret = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                ret.append(node.val)
                
            else:
                if node.right: stack.append((node.right, False))
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
            
        return ret

        '''
        # ==================================================
        #  Binary Tree + In-order Traversal               =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        '''
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */

    public List<Integer> inorderTraversal(TreeNode root) {
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
                if(node.right != null) stack.push(new Pair<TreeNode, Boolean>(node.right, false));
                stack.push(new Pair<TreeNode, Boolean>(node, true));
                if(node.left != null) stack.push(new Pair<TreeNode, Boolean>(node.left, false));
            }
        }
        
        return result;
    }
}
```