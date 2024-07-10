from collections import deque

class Graph:
    def __init__(self):
        self.adjacencylist = {}
    def add_vertex(self,vertex):
        if vertex not in self.adjacencylist.keys():
            self.adjacencylist[vertex]=[]
            return True
        return False
    def print_graph(self):
        for i in self.adjacencylist:
            print(i,':',self.adjacencylist[i])
    def add_edge(self,v1,v2):
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
    
    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adj_vertex in self.adjacencylist[current_vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)

    def dfs(self,vertex):
        visited = set()
        #visited.add(vertex)
        stack = [vertex]
        while stack:
            curr_ver = stack.pop()
            if curr_ver not in visited:
                visited.add(curr_ver)
                print(curr_ver)
            for adj_v in self.adjacencylist[curr_ver]:
                if adj_v not in visited:
                    stack.append(adj_v)


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
# my_graph.add_edge("A", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "E")
my_graph.print_graph()
my_graph.dfs("A")
