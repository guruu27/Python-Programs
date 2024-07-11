class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        else:
            self.gdict = gdict

    def shortpath(self,start,end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path [ -1 ]
            if node  ==  end:
                return path
            for adjnodes in self.gdict.get(node,[]):
                new_path = list(path)
                new_path.append(adjnodes)
                queue.append(new_path)
        #print(path)


customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g = Graph(customDict)
print(g.shortpath("a", "f"))