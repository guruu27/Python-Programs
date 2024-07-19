import heapq

class Edge:
    def __init__(self,weight,startv,targetv):
        self.weight = weight
        self.startv = startv
        self.targetv = targetv

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        # previous node
        self.predecessor = None
        self.min_dis = float("inf")
        self.neighbors = []
    
    def __lt__(self,other_node):
        return self.min_dis < other_node.min_dis
    
    def add_edge(self,weight,destinationv):
        edge = Edge(weight,self,destinationv)
        self.neighbors.append(edge)

class DijkstraAlgorithm:
    def __init__(self):
        self.heap = []

    def calculate(self,startv):
        startv.min_dis = 0
        heapq.heappush(self.heap,startv) 
        while self.heap:
            actualv = heapq.heappop(self.heap)
            if actualv.visited:
                continue
            for edge in actualv.neighbors:
                start_v = edge.startv
                target_v = edge.targetv
                new_dis = start_v.min_dis + edge.weight
                if new_dis < target_v.min_dis:
                    target_v.min_dis = new_dis
                    target_v.predecessor = start_v
                    heapq.heappush(self.heap,target_v)
            actualv.visited = True
    
    def shortp(self,vertex):
        print(f"Short Path{vertex.min_dis}")
        av = vertex
        if av is not None:
            print( av.name ,end=" ")
            av = av.predecessor



# Step 1 - create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Step 2 - create edges
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = DijkstraAlgorithm()
algorithm.calculate(nodeA)
algorithm.shortp(nodeG)
