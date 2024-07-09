class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict = gdict
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    
graph = Graph({
    "a":["b","c"],
    "b":["c","e"]
})

graph.addEdge("b","u")

print(graph.gdict)