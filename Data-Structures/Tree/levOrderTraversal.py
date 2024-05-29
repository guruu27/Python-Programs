class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.leftChild = None
        self.rightChild =  None


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


  
levOrderTraversal(newBT)
