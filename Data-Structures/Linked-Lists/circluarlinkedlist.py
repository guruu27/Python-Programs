class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class CSLinkdedList:
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
         
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        
        self.length+=1
    def __str__(self) -> str:
         temp = self.head
         result=""
         while temp is not None:
             result+=str(temp.value)+"-->"
             temp = temp.next
             if temp == self.head:
                 break
         return result

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length +=1
    def insert(self,value,index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            raise Exception("Invalid index")
        

        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = new_node
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif self.length == index:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp ==  self.head:
                break

    def search(self,value):
        temp = self.head
        idx = 0
        while temp is not None:
            if temp.value == value:
                return idx
            temp = temp.next
            idx+=1
        return -1
    def get(self,idx):
        temp = self.head
        if idx == -1:
            return self.tail.value
        if idx>self.length or idx<0:
            return("Invalid Index")
        for _ in range(idx-1):
            temp = temp.next
        return temp.next
    def set_value(self,idx,value):
        temp = self.head
        if idx>self.length or idx<0:
            return("Invalid Index")
        if idx == -1:
            self.tail.value = value
        for _ in range(idx-1):
            temp = temp.next
        temp.next.value = value
    def popfirst(self):
        if self.length == 0:
            return None
        pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            pop.next = None
        self.length -= 1
        return pop.value
    def pop(self):
        if self.length == 0:
            return None
        pop1 = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
        pop1.next = None
        self.length -= 1
        return pop1.value
    def remove(self,index):
        if index == 0:
            return self.popfirst()
        if index < 0 or index >= self.length:
            return None
        if index == -1 or index == self.length -1:
            return self.pop()
        prev = self.get(index-1)
        pop = prev.next
        prev.next = pop.next
        pop.next = None
        self.length -= 1
        return pop
    def delete_all(self):
        self.head = self.tail = None
        self.length = 0


        

csLinkdedList = CSLinkdedList()
csLinkdedList.append(1)
csLinkdedList.append(2)
csLinkdedList.append(3)
csLinkdedList.prepend(99)
csLinkdedList.insert(10,4)
#csLinkdedList.traverse()
csLinkdedList.set_value(3,20)
print(csLinkdedList.remove(2))
csLinkdedList.delete_all()
print(csLinkdedList)
