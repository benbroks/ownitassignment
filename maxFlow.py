# Credits to @bigbighd604
# See: https://github.com/bigbighd604/Python/blob/master/graph/Ford-Fulkerson.py


class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.target = v
    self.capacity = w

  def __repr__(self):
    return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
    def  __init__(self):
        self.adj = {}
        self.flow = {}

    def AddVertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def GetEdges(self, v):
        return self.adj[v]

    def AddEdge(self, u, v, w = 0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        # Intialize all flows to zero
        self.flow[edge] = 0
        self.flow[redge] = 0

    def FindPath(self, source, target, path):
        if source == target:
            return path
        edges = self.GetEdges(source)
        for edge in edges:
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge, residual) in path:
                result = self.FindPath(edge.target, target, path + [(edge, residual)])
                if result != None:
                    return result
        return None

    def MaxFlow(self, source, target):
        path = self.FindPath(source, target, [])
        print(path)
        while path != None:
            flow = min(res for edge, res in path)
            for edge, _ in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.FindPath(source, target, [])
            print(path)
        for key in self.flow:
            if self.flow[key] > 0:
                print('%s:%s' % (key,self.flow[key]))
        return sum(self.flow[edge] for edge in self.GetEdges(source))



