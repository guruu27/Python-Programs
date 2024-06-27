
import QueueLinkedList as queue

class AVL:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrderTraversal(rootNode):
    if not rootNode:
        return "Empty"
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTravesal(rootNode):
    if not rootNode:
        return "Empty"
    else:
        inOrderTravesal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTravesal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return "Empty"
    else:
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

def levOrderTraversal(rootNode):
    if not rootNode:
        return "Empty"
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not(customq.isEmpty()):
            root = customq.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customq.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customq.enqueue(root.value.rightChild)

def searchNode(rootNode,nodevalue):
    if not rootNode:
        return "Empty"
    if rootNode.data == nodevalue:
        return "Found", rootNode.data
    elif nodevalue<=rootNode.data:
        if rootNode.leftChild.data == nodevalue:
            return "Found", rootNode.leftChild.data
        else:
            searchNode(rootNode.leftChild,nodevalue)
    else:
        if rootNode.rightChild.data == nodevalue:
            return "Found", rootNode.rightChild.data
        else:
            searchNode(rootNode.rightChild,nodevalue)

def getheight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightrotate(disbalanceNode):
    newroot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild 
    newroot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getheight(disbalanceNode.leftChild),getheight(disbalanceNode.rightChild))
    newroot.height = 1 + max(getheight(newroot.leftChild),getheight(newroot.rightChild))
    return newroot

def leftrotate(disbalanceNode):
    newroot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newroot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getheight(disbalanceNode.leftChild),getheight(disbalanceNode.rightChild))
    newroot.height = 1 + max(getheight(newroot.leftChild),getheight(newroot.rightChild))
    return newroot

def getbalance(rootNode):
    if not rootNode:
        return 0
    return getheight(rootNode.leftChild) - getheight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVL(nodeValue)
    elif rootNode.data < nodeValue:
        rootNode.rightChild = insertNode(rootNode.rightChild,nodeValue)
    else:
        rootNode.leftChild = insertNode(rootNode.leftChild,nodeValue)    
    rootNode.height = 1 + max(getheight(rootNode.leftChild),getheight(rootNode.rightChild))
    balance = getheight(rootNode.leftChild) - getheight(rootNode.rightChild)
    if balance>1 and nodeValue < rootNode.leftChild.data:
        return  rightrotate(rootNode)
    if balance>1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftrotate(rootNode.leftChild)
        return rightrotate(rootNode)
    if balance<-1 and nodeValue > rootNode.rightChild.data:
        return leftrotate(rootNode)
    if balance<-1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightrotate(rootNode.rightChild)
        return leftrotate(rootNode)
    return rootNode


def getMin(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMin(rootNode.leftChild)

def deleteNode(rootNode,nodeValue):
    if not rootNode:
        return rootNode
    elif rootNode.data < nodeValue:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    elif rootNode.data > nodeValue:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)    
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rigtChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp =  getMin(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
    balance = getbalance(rootNode)
    if balance>1 and getbalance(rootNode.leftChild)>=0:
        return  rightrotate(rootNode)
    if balance>1 and getbalance(rootNode.leftChild)<0:
        rootNode.leftChild = leftrotate(rootNode.leftChild)
        return rightrotate(rootNode)
    if balance<-1 and getbalance(rootNode.rightChild)<=0:
        return leftrotate(rootNode)
    if balance<-1 and getbalance(rootNode.rightChild)>0:
        rootNode.rightChild = rightrotate(rootNode.rightChild)
        return leftrotate(rootNode)
    return rootNode





newAVL = AVL(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levOrderTraversal(newAVL)
