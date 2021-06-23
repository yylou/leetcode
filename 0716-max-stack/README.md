# Problem
[716. Max Stack](https://leetcode.com/problems/max-stack/)

# Performance
![result](./result.png)

# Python
```Python3
class MaxStack:
    # ==================================================
    #  Python built-in List                            =
    # ==================================================
    #  time  : O(1) for all operations excepting 'popMax' which is O(n)
    #  space : O(n)
    
    def __init__(self):
        self.size  = 0
        self.stack = []
        
    def push(self, x: int) -> None:
        if not self.stack: 
            self.stack.append((x, 0))
        else:
            maxIndex = self.size if x >= self.stack[self.stack[-1][1]][0] else self.stack[-1][1]
            self.stack.append((x, maxIndex))
            
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[self.stack[-1][1]][0]

    def popMax(self) -> int:
        self.size -= 1
        maxIndex = self.stack[-1][1]
        maxVal = self.stack.pop(maxIndex)[0]
        
        #  Renew each element's local Max value
        for i in range(maxIndex, self.size):
            if i == 0: self.stack[i] = (self.stack[i][0], i)
            else:
                if self.stack[i][0] >= self.stack[self.stack[i-1][1]][0]:
                    self.stack[i] = (self.stack[i][0], i)
                else:
                    self.stack[i] = (self.stack[i][0], self.stack[i-1][1])
        
        return maxVal
```

```Python3
class Node:
    def __init__(self, val, max, next, prev):
        self.val  = val
        self.max  = max
        self.next = next
        self.prev = prev

class MaxStack:
    # ==================================================
    #  Double Linked-List                              =
    # ==================================================
    #  time  : O(1) for all operations excepting 'popMax' which is O(n)
    #  space : O(n)

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        if not self.head: 
            self.head = Node(x, x, None, None)
            self.tail = self.head
        else: 
            tmpNode = Node(x, max(x, self.head.max), self.head, None)
            self.head.prev = tmpNode
            self.head = tmpNode

    def pop(self) -> int:
        curVal = self.head.val 
        
        self.head = self.head.next
        if self.head: self.head.prev = None
        
        return curVal

    def top(self) -> int:
        return self.head.val

    def peekMax(self) -> int:
        return self.head.max

    def popMax(self) -> int:
        curMax = self.head.max
        
        #  Remove the node with 'curMax' value
        target = self.head
        while target.val != curMax: target = target.next
        
        #  (1) stack only has one element
        if target == self.head and target == self.tail:
            self.head = None
            self.tail = None
        
        #  (2) target node is at the head
        elif target == self.head and target != self.tail:
            self.head = self.head.next
            self.head.prev = None
            
        #  (3) target node is at the tail
        elif target != self.head and target == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        
        #  (4) target node is between the head and the tail
        else:
            target.prev.next = target.next
            target.next.prev = target.prev
            
        #  Renew each node's localMax value
        if self.tail:
            tail = self.tail
            localMax = tail.val
            while tail:
                tail.max = max(tail.val, localMax)
                localMax = tail.max
                tail = tail.prev
        
        return curMax
```

# Java (ongoing)
```Java
```
