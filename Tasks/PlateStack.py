class PlateStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = []

    def __str__(self):
        return str(self.stack)
    
    def push(self,item):
        if len(self.stack)>0 and len(self.stack[-1])< self.capacity:
            self.stack[-1].append(item)
        else:
            self.stack.append([item])
    
    def pop(self):
        while len(self.stack) and len(self.stack[-1]) == 0:
            self.stack.pop()
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1].pop()
    
    def pop_at(self,stack_num):
        if len(self.stack[stack_num])>0:
            return self.stack[stack_num].pop()
        else:
            return None

customStack= PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
