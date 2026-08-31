class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, val: int) -> None:
        if not self.MinStack:
            self.MinStack.append([val, val])
        else:
            self.MinStack.append([val, min(self.getMin(), val)])

    def pop(self) -> None:
        self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1][0]

    def getMin(self) -> int:
        return self.MinStack[-1][1]