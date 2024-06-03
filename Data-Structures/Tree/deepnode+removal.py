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


def getdeepestnode(rootNode):
    if not rootNode:
        return "None"
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            if root.value.leftChild is not None:
                
                customq.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                
                customq.enqueue(root.value.rightChild)
            
            dnode = root.value

        return dnode
            
DNode = getdeepestnode(newBT)

def deldeepnode(rootNode):
    if not rootNode:
        return "Empty"
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            if root.value == DNode:
                root.value = None
            if root.value.leftChild is not None:
                if root.value.leftChild == DNode:
                    root.value.leftChild = None
                else:
                    customq.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                if root.value.rightChild == DNode:
                    root.value.rightChild = None
                else:
                    customq.enqueue(root.value.rightChild)
            

deldeepnode(newBT)
postOrderTraversal(newBT)
