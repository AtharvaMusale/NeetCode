class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self,val):
        self.stack.append(val)
        if not self.minstack:
            val = min(val,val)
        
        else:
            val = min(val, self.minstack[-1])
        
        self.minstack.append(val)

    
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1]

    # def __init__(self):
    #     self.stack = []
    #     self.minstack = []
        
    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minstack:
    #         val = min(val,val)
    #     else:
    #         val = min(val,self.minstack[-1])
    #     self.minstack.append(val)


    # def pop(self) -> None:
    #     self.minstack.pop()
    #     self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minstack[-1]
        
