class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = 0

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minElement = x
        else:
            if x >= self.minElement:
                self.stack.append(x)
            elif x < self.minElement:
                compFlag = 2 * x - self.minElement
                self.stack.append(compFlag)
                self.minElement = x

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            if self.stack[-1] >= self.minElement:
                self.stack.pop()
            elif self.stack[-1] < self.minElement:
                getValue = 2*self.minElement - self.stack[-1]
                self.minElement = getValue
                self.stack.pop()

    @property
    def top(self) -> int:
        if len(self.stack ==0):
            return -1
        else:
            if self.stack[-1]>=self.minElement:
                return  self.stack[-1]
            elif self.stack[-1]<self.minElement:
                return self.minElement

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.minElement


obj = MinStack()
obj.push(5)
obj.push(7)
obj.push(3)
first = obj.getMin()
obj.pop()
obj.pop()
first = obj.getMin()

obj.pop()

obj.pop()