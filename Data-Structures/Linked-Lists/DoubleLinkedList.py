class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)#f"{self.prev}<-{self.value}->{self.next}"

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0




    def __str__(self):
        temp = self.head
        res = ""
        while temp is not None:
            res += str(temp)
            if temp.next is not None:
                res+="<->"
            temp = temp.next
        return res
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.append(value)
        temp = self.head
        temp.prev = new_node
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def revtraverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.value)
            temp = temp.prev

    def search(self,target):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == target:
                return index
            temp = temp.next
            index+=1
        return -1

    def get(self,idx):
        if idx < 0 or idx >= self.length:
            return None
        if idx < self.length // 2:
            curr = self.head
            for _ in range(idx-1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length-1, idx,-1):
                curr = curr.prev 
        return curr
    

    def set_value(self,idx,value):
        if idx < 0 or idx >= self.length:
            return False
        temp = self.get(idx)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,idx,value):
        new = Node(value)
        if self.length == 0:
            self.head = new
            self.tail = new
        else:
            curr = self.head
            for _ in range(idx-1):
                curr = curr.next
            temp = curr.next
            new.next = curr.next
            new.prev = curr
            curr.next = new
            temp.prev = new


    def popfirst(self):
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr =  temp.next
            curr.prev = None
            self.head = temp.next
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp
    def pop(self):
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr = temp.prev
            curr.next = None
            self.tail = curr
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp
    def remove(self,idx):
        pop = self.get(idx)
        pop.prev.next=pop.next
        pop.next.prev = pop.prev
        pop.next = pop.prev = None
        self.length-=1
        return pop
    


    
dll = DoubleLinkedList()
#dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.prepend(00)
print(dll.popfirst())
print(dll)
