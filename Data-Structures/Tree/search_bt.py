import QueueLinkedList as queue

class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.leftChild = None
        self.rightChild =  None

    # def __str__(self, level = 0):
    #     ret = " " * level + str(self.data) + "\n"
    #     for child in self.children:
    #         ret += child.__str__(level+1)
    #     return ret
    # def addChild(self,TreeNode):
    #     self.children.append(TreeNode)

newBT = TreeNode("Drinks")
lC = TreeNode('Hot')
rC = TreeNode('Cold') 
lClC = TreeNode('Tea')
lCrC = TreeNode('coffee')
rClC = TreeNode('pepsi')
rCrC = TreeNode('cola')

newBT.leftChild = lC
newBT.rightChild = rC
lC.leftChild = lClC
lC.rightChild = lCrC
rC.leftChild = rClC
rC.rightChild = rCrC


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customq.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customq.enqueue(root.value.rightChild)


  

def search_bt(rootNode,targ):
    if not rootNode:
        return
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            if root.value.data == targ:
                return "Success: ", root
            if root.value.leftChild is not None:
                customq.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customq.enqueue(root.value.rightChild)
             
        return "Not Found"


search_bt(newBT,"Tea")
