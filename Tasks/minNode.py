class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
    def __str__(self,value):
        string = str(self.value)
        if self.next:
            string += "," + str(self.next)
        return string
    
class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None
    
    def min(self):
        if self.minNode:
            return self.minNode.value
        else:
            None

    def push(self,item):
        if self.minNode and (self.minNode.value<item):
            self.minNode = Node(value=self.minNode.value,next = self.minNode)
        else:
            self.minNode = Node(value=item,next = self.minNode)
        self.top = Node(value=item,next = self.top)
    
    def pop(self):
        if self.top:
            self.minNode = self.minNode.next
            val = self.top
            self.top = self.top.next
            return val
        else:
            return None
    
customStack = Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())
customStack.pop()
print(customStack.min())
        
            
