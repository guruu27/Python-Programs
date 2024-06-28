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
    


def heapifyextractmethod(rootNode,index,heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapsize < leftIndex:
        return
    elif rootNode.heapsize == leftIndex:
        if heapType=='Min':
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            else:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
     else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyextractmethod(rootNode, swapChild, heapType)
    
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyextractmethod(rootNode, 1, heapType)
        return extractedNode   




newBinaryHeap = Heap(5)
insertnode(newBinaryHeap,4,'Max')
insertnode(newBinaryHeap,5,'Max')
insertnode(newBinaryHeap,3,'Max')
insertnode(newBinaryHeap,2,'Max')

levelordertaversal(newBinaryHeap)