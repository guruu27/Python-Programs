class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next= None
class cdll:
    def __init__(self):
        self.tail = None
        self.head = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    #create
    def create(self,value):
        new = Node(value)
        self.head = new
        self.tail = new
        new.prev = new
        new.next = new
        return "The CDLL is created successfully"
    #insertion
    def insert(self,idx,value):
        if self.head is None:
            return " Not exists "
        new = Node(value)
        if idx == 0:
            new.next = self.head
            self.head.prev = new
            new.prev = self.tail
            self.tail.next = new
            self.head = new
        elif idx == -1:
            new.prev = self.tail
            self.tail.next = new
            new.next = self.head
            self.head.prev = new
            self.tail = new
        else:
            temp = self.head
            index = 0
            for _ in range(idx-1):
                temp = temp.next
            new.next = temp.next
            temp.next = new
            new.prev = temp
            new.next.prev = new
        return "Done"
    #traverse
    def traverse(self):
        if self.head is None:
            return "Empty"
        temp = self.head
        while temp:
            print(temp.value)
            if temp == self.tail:
                break
            temp = temp.next
    def revtraverse(self):
        if self.head is None:
            return "Empty"
        temp = self.tail
        while temp:
            print(temp.value)
            if temp == self.head:
                break
            temp = temp.prev
    def search(self,value):
        if self.head is None:
            return "Empty"
        temp = self.head
        while temp:
            if temp.value == value:
                return "Found"
            elif temp == self.tail:
                return "Not Found"
            temp = temp.next
    def delnode(self,id):
        if self.head is None:
            return " Empty "
        if id == 0:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
        elif id == -1:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
        else:
            temp = self.head
            idx = 0
            for _ in range(id-1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp
        return "Done"
    def deleteall(self):
        if self.head is None:
            return "Empty"
        else:
            self.tail.next = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None


































circularDLL = cdll()
circularDLL.create(5)
circularDLL.insert(0,1)
circularDLL.insert(1,2)
circularDLL.insert(2,3)
print([node.value for node in circularDLL])
circularDLL.traverse()
circularDLL.revtraverse()
print(circularDLL.search(30))
