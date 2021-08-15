from collections import defaultdict

class Graph(object):
  def __init__(self, edges):
    # Initilizes base structure
    self.adj = defaultdict(set)
    self.fill_edges(edges)

  def get_vertex(self):
    # Returns the list of vertexes 
    return list(self.adj.keys())


  def get_edges(self):
    # Returns the list of edges
    return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


  def fill_edges(self, edges):
    # Fill the graph with edges
    for u, v in edges:
        self.add_edge(u, v)

  def add_edge(self, u, v):
    # Add the edge between given vertexes
    self.adj[u].add(v)
    self.adj[v].add(u)

  def check_edge(self, u, v):
    # Checks if there is an edge between given vertexes
    return u in self.adj and v in self.adj[u]


  def __len__(self):
    return len(self.adj)


  def __str__(self):
    return '{}({})'.format(self.__class__.__name__, dict(self.adj))


  def __getitem__(self, v):
    # Makes it possible to call graph[v] and get the list of neighbors to a vertex
    return self.adj[v]


# This class was based on the following implementation: https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/