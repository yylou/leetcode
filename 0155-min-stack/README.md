# Problem
[155. Min Stack](https://leetcode.com/problems/min-stack)

# Performance
![result](./result.png)
![result-java](./result-java.png)

# Python
```Python3
class MinStack:
    # ==================================================
    #  Python built-in List                            =
    # ==================================================
    # time  : O(1) for all operations
    # space : O(n)

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: self.stack.append((val, val))
        else: self.stack.append((val, min(val, self.stack[-1][1])))
                               
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

```Python3
class Node:
    def __init__(self, val, min, next):
        self.val  = val
        self.min  = min
        self.next = next

class MinStack:
    # ==================================================
    #  Single Linked-List                              =
    # ==================================================
    # time  : O(1) for all operations
    # space : O(n)

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head: self.head = Node(val, val, None)
        else: self.head = Node(val, min(val, self.head.min), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
```

# Java
```Java
class MinStack {
    /**
     * @time  : O(1) for all operations
     * @space : O(n)
     */
    
    private class Node {
        int val;
        int min;
        Node next;
        
        private Node(int val, int min, Node next) {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }
    
    private Node head;
    
    public MinStack() {
        
    }
    
    public void push(int val) {
        if(head == null) {
            head = new Node(val, val, null);
        } else {
            head = new Node(val, Math.min(val, head.min), head);
        }
    }
    
    public void pop() {
        head = head.next;
    }
    
    public int top() {
        return head.val;
    }
    
    public int getMin() {
        return head.min;
    }
}
```
