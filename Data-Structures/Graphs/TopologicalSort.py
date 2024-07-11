from collections import defaultdict

class Graph:
    def __init__(self, verticesList):
        self.graph = defaultdict(list)
        self.verticesList = verticesList
    def addEdge(self,v,edge):
        self.graph[v].append(edge)
    def TopHelper(self,v,visited,stack):
        
        visited.append(v)

        for adjv in self.graph[v]:
            if adjv not in visited:
                self.TopHelper(adjv,visited,stack)
        
        stack.insert(0,v)
    def TopSort(self):
        stack = []
        visited = []
        for i in list(self.graph):
            if i not in visited:
                self.TopHelper(i,visited,stack)
        print(stack)

customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.TopSort()