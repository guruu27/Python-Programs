
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofstr = False

class Trie:
    def __init__(self):
        self.root  = TrieNode()
    
    def insertstring(self,word):
        curr = self.root
        for i in word:
            ch = i
            node =  curr.children.get(ch)
            if node == None:
                node = TrieNode()
                curr.children.update({ch:node})
            curr =  node
        curr.endofstr = True
        print("Done")




    def searchstring(self,word):
        curr = self.root
        for i in word:
            ch = i
            node =  curr.children.get(ch)
            if node == None:
                print("The word does not exist")
                return False
            curr = node
        if curr.endofstr == True:
            return True
        else:
            return False
        
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endofstr = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endofstr == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


        
newTrie = Trie()
newTrie.insertstring("App")
newTrie.insertstring("Appl")
print(newTrie.searchstring("Appl"))
deleteString(newTrie.root,"App",0)
