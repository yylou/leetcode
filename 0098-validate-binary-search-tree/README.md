# Problem
[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)

# Performance
![result-python](./result.png)
![result-java](./result-java.png)

# Python
```Python3
# Iterative Solution

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #: (base case)
        if not root.left and not root.right: return True
        
        # ==================================================
        #  Tree + DFS + Stack                (Iterative)   =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            
            if node.val >= upper or node.val <= lower: return False
            
            #: (left  sub-tree) set UPPER bound to current node's value (<= curValue)
            #: (right sub-tree) set LOWER bound to current node's value (>= curValue)
            if node.left : stack.append( (node.left,  lower,    node.val) )
            if node.right: stack.append( (node.right, node.val, upper) )
                
        return True
```

```Python3
# Recursive Solution

class Solution:
    def _isValidBSTHelper(self, node, lower, upper):
        if not node: return True
        
        if ((upper > node.val > lower)                              and
            self._isValidBSTHelper(node.left,  lower,    node.val ) and
            self._isValidBSTHelper(node.right, node.val, upper)):
            return True
        
        return False
    
    def isValidBST(self, root: TreeNode) -> bool:
        #: (base case)
        if not root.left and not root.right: return True
        
        # ==================================================
        #  Tree + DFS + Stack                (Recursive)   =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        return self._isValidBSTHelper(root, float('-inf'), float('inf'))
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
     
    public boolean isValid(TreeNode node, long lower, long upper) {
        if(node == null) return true;
        
        return (lower < node.val && node.val < upper) &&
               isValid(node.left, lower, node.val)    && 
               isValid(node.right, node.val, upper);
    }
    
    public boolean isValidBST(TreeNode root) {
        if(root.left == null && root.right == null) return true;
        
        return isValid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
```
