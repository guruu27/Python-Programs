
import QueueLinkedList as queue

class AVL:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# def insertNode(rootNode,nodev):
#     if rootNode.data == None:
#         rootNode.data = nodev
#     elif nodev <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild = AVL(nodev)
#         else:
#             insertNode(rootNode.leftChil d,nodev)
#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild = AVL(nodev)
#         else:
#             insertNode(rootNode.rightChild,nodev)
#     return "Done"


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

def minval(rootNode):
    curr = rootNode
    while curr.leftChild is not None:
        if rootNode.leftChild:
            curr = curr.leftChild
    return curr.data



newBST = BSTNode(None) 
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
levOrderTraversal(newBST)
print(minval(newBST))
