class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.leftChild = None
        self.rightChild =  None


newBT = TreeNode("Drinks")
lC = TreeNode('Hot')
rC = TreeNode('Cold') 
newBT.leftChild = lC
newBT.rightChild = rC


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBT)
