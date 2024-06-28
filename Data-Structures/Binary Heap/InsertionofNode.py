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


def heapifyTreeInsert(rootNode,index,heapType):
    parentindex = int(index/2)
    if index<=1:
        return
    if heapType == 'Min':
        if rootNode.customList[index] < rootNode.customList[parentindex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentindex]
            rootNode.customList[parentindex] = temp
        heapifyTreeInsert(rootNode,parentindex,heapType)
    elif heapType == 'Max':
        if rootNode.customList[index] > rootNode.customList[parentindex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentindex]
            rootNode.customList[parentindex] = temp
        heapifyTreeInsert(rootNode,parentindex,heapType)

def insertnode(rootNode, nodeval, heapType):
    if rootNode.heapsize+1 == rootNode.maxsize:
        return "Full"
    rootNode.customList[rootNode.heapsize + 1] = nodeval
    rootNode.heapsize+=1
    heapifyTreeInsert(rootNode,rootNode.heapsize,heapType)
    return "Done"
    
newBinaryHeap = Heap(5)
insertnode(newBinaryHeap,4,'Max')
insertnode(newBinaryHeap,5,'Max')
insertnode(newBinaryHeap,3,'Max')
insertnode(newBinaryHeap,2,'Max')

levelordertaversal(newBinaryHeap)