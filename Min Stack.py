class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.currmin = None
        

    def push(self, val: int) -> None:
        if self.currmin == None or val < self.currmin :
            self.currmin = val
            self.minstack.append(val)
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.minstack.append(self.currmin)

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())