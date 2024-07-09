class Graph:
    def __init__(self):
        self.adjacencylist = {}
    def addvertex(self,vertex):
        if vertex not in self.adjacencylist.keys():
            self.adjacencylist[vertex]=[]
            return True
        return False
    def printgraph(self):
        for i in self.adjacencylist:
            print(i,':',self.adjacencylist[i])
    def addEdge(self,v1,v2):
        if v1 in self.adjacencylist.keys() and v2 in self.adjacencylist.keys():
            self.adjacencylist[v1].append(v2)
            self.adjacencylist[v2].append(v1)
            return True
        return False
    def removeEdge(self,v1,v2):
        if v1 in self.adjacencylist.keys() and v2 in self.adjacencylist.keys():
            try:  
                self.adjacencylist[v1].remove(v2)
                self.adjacencylist[v2].remove(v1)
            except:
                pass
            return True
        return False
        def remove_vertex(self, vertex):
            if vertex in self.adjacency_list.keys():
                for other_vertex in self.adjacency_list[vertex]:
                    self.adjacency_list[other_vertex].remove(vertex)
                del self.adjacency_list[vertex]
                return True
            return False

        
cl = Graph()
cl.addvertex("A")
cl.addvertex("B")
cl.addvertex("C")
cl.addEdge("A","B")
cl.addEdge("A","C")
cl.addEdge("C","B")
cl.printgraph()
print("After removal")
cl.removeEdge("A","C")
cl.addvertex("D")
cl.printgraph()