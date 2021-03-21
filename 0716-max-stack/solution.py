class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append( (x, self.size) )
        else:
            maxIndex = self.size if x >= self.stack[self.stack[-1][1]][0] else self.stack[-1][1]
            self.stack.append( (x, maxIndex) )

        self.size += 1


    def pop(self):
        """
        :rtype: int
        """
        self.size -= 1
        return self.stack.pop()[0]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]


    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[self.stack[-1][1]][0]


    def popMax(self):
        """
        :rtype: int
        """
        self.size -= 1
        maxIndex = self.stack[-1][1]
        maxVal = self.stack.pop( self.stack[-1][1] )[0]

        ##  refresh each item's MAX index
        for i in xrange( maxIndex, self.size ):
            if i == 0: self.stack[i] = (self.stack[i][0], i)
            else:
                if self.stack[i][0] >= self.stack[self.stack[i-1][1]][0]:
                    self.stack[i] = (self.stack[i][0], i)
                else:
                    self.stack[i] = (self.stack[i][0], self.stack[i-1][1])

        return maxVal


##  Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
