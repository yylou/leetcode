class MinStack:
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


'''
Java Solution
==================================================================================================
class MinStack {
    /**
     * @time  : O(1) for all operations
     * @space : O(n)
     */

    private Stack<int[]> stack;
    
    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if(stack.isEmpty()) {
            stack.push(new int[]{val, val});
        } else {
            int curMin = stack.peek()[1];
            stack.push(new int[]{val, Math.min(val, curMin)});
        }
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek()[0];
    }
    
    public int getMin() {
        return stack.peek()[1];
    }
}
==================================================================================================
'''
