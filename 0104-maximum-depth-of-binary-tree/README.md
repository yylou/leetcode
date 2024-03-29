# Problem
[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # (base case)
        if not root: return 0
        if not root.left and not root.right: return 1
    
        # ==================================================
        #  Binary Tree                       (Iterative)   =
        # ==================================================
        # time  : O(n)
        # space : O(n), O(log(n)) for average case

        maxDepth = 0
        stack = [root]
        
        while stack:
            # loop through stack for current length, pop the first node
            for i in range(len(stack)):
                node = stack.pop( 0 )
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                    
            maxDepth += 1
            
        return maxDepth
```

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #: (base case)
        if not root: return 0
        if not root.left and not root.right: return 1
        
        # ==================================================
        #  Binary Tree                       (Recursive)   =
        # ==================================================
        # time  : O(n)
        # space : O(n), O(log(n)) for average case
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

# Java
```Java
class Solution {
    /**  
     * @time  : O(n)
     * @space : O(n), O(log(n)) for average case
     */

    public int maxDepth(TreeNode root) {
        /* base case */
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        
        int maxDepth = 0;
        Queue<TreeNode> stack = new LinkedList<>();
        stack.add(root);
        
        while(!stack.isEmpty()) {
            int size = stack.size();
            
            for(int i=0 ; i<size ; i++) {
                TreeNode node = stack.remove();
                
                if(node.left != null) stack.add(node.left);
                if(node.right != null) stack.add(node.right);
            }
            
            maxDepth++;
        }
        
        return maxDepth;
    }
}
```
