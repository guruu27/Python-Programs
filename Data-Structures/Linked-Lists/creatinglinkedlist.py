class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head= None
    def insert(self,newnode):
        if self.head is None:
            self.head= newnode
        else:
            lastnode= self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode
    def printit(self):
        currentnode= self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next
            
        
        
node = Node("John")
linkedlist= LinkedList()
linkedlist.insert(node)
node1= Node("Dev")
linkedlist.insert(node1)
linkedlist.printit()
