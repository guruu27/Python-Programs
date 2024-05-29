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


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(newBT)
