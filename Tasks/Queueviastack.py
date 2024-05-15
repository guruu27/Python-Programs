class Stack:
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def push(self, item):
        self.list.append(item)
    def pop (self):
        if self.list:
            return self.list.pop()
        else:
            return None
    
class Queueviastack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enqueue(self,item):
        self.stack1.push(item)

    def dequeue(self):
        while len(self.stack1):
            self.stack2.push(self.stack1.pop())
        res = self.stack2.pop()
        while len(self.stack2):
            self.stack1.push(self.stack2.pop())
        return res

customQueue = Queueviastack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())
