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

def insert_bt(rootNode,new_node):
    if not rootNode:
        rootNode = new_node
    else:
        customq = queue.Queue()
        customq.enqueue(rootNode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            if root.value.leftChild is not None:
                customq.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = new_node
                return "Success"
            if root.value.rightChild is not None:
                customq.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = new_node
                return "Success"

newnode = TreeNode("Kitty")
insert_bt(newBT,newnode)
