class MinStack:

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)
        # if x < self.minimum:
        #     self.minimum = x

    def pop(self) -> None:
        ret = self.lst.pop()


    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
        myMin = math.inf
        if self.lst:
            for i in range(len(self.lst)):
                if myMin>self.lst[i]:
                    myMin = self.lst[i]
            return myMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()