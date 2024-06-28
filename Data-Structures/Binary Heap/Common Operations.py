class Heap:
    def __init__(self,size):
        self.customList = (size+1) * [None]
        self.maxsize = size + 1
        self.heapsize = 0

def peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def size(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapsize

def levelordertaversal(rootNode):
    if not rootNode:
        return 
    else:
        for i in range(1,rootNode.heapsize+1):
            print(rootNode.customList[i])


newBinaryHeap = Heap(5)
print(size(newBinaryHeap))