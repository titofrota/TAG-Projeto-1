#################################################
# Universidade de Brasília - UnB                #
# Departamento de Ciência da Computação         #
# Teoria e Aplicação de Grafos - 2021/1         #
# Ítalo Frota - 18/0019279                      #
#################################################

import GraphClass
import random

def main():
  with open("soc-dolphins.txt") as f:
      lines = f.read().strip().split("\n")

  edges = []

  for line in lines:                # Format the edges list
      ls = line.split(" ")
      edges.append((ls[0], ls[1]))

  graph = GraphClass.Graph(edges)   # Generates the graph

  p = graph.get_vertex()            # Initializes p with all the vertexes
  r = []
  x = []

  print("Without pivoting:")
  bron_kerbosch(p, r, x, graph)

  p = graph.get_vertex()            # Re-initializes p with all the vertexes
  r = []
  x = []
  print("\nWith pivoting:")
  bron_kerbosch_with_pivot(p, r, x, graph)

  p = graph.get_vertex()            # Re-initializes p with all the vertexes
  coefficient(p, graph)


def bron_kerbosch(p, r, x, graph):  # Executes the algorithm without pivoting
  if not any((p, x)):               # If p and x are empty, r is a maximal clique
    print(r)
  for v in p[:]:
    r2 = r + [v]
    p2 = [val for val in p if val in graph[v]]    #  P is restricted to the neighbour set of v
    x2 = [val for val in x if val in graph[v]]    #  X is restricted to the neighbour set of v
    bron_kerbosch(p2, r2, x2, graph)              # Recursive call 
    p.remove(v)
    x.append(v)

def bron_kerbosch_with_pivot(p, r, x, graph):  # Executes the algorithm with pivoting
  if not any((p, x)):               # If p and x are empty, r is a maximal clique
    print(r)

  try:
    u = random.choice(list(set(p).union(x)))      # Choose a random vertex u from p union x
    z = list(set(p).difference(graph[u]))         #
  except IndexError:                # If P union X is empty        
    z = p
  
  for v in z[:]:
    r2 = r + [v]
    p2 = [val for val in p if val in graph[v]]    #  P is restricted to the neighbour set of v
    x2 = [val for val in x if val in graph[v]]    #  X is restricted to the neighbour set of v
    bron_kerbosch_with_pivot(p2, r2, x2, graph)        # Recursive call 
    p.remove(v)
    x.append(v)

def coefficient(p, graph):
  local_coefficient = {}
  medium_coefficient = 0.0

  for v in p:
    neighbours = graph[v]                         # Gets v neighbour set
    neighbours_count = len(neighbours)            # Counts the number of neighbours
    edges_count = 0
    
    if neighbours_count > 1:
      for v1 in neighbours:
        for v2 in neighbours:
          if graph.check_edge(v1,v2):       # Checks if there is a edge between v1 and v2
            edges_count += 1

      edges_count /= 2 
      local_coefficient[v] = (2 * edges_count) / (neighbours_count * (neighbours_count - 1))     # Calculates the local clustering coefficient
    else:
      local_coefficient[v] = 0

    medium_coefficient += local_coefficient[v]

  print("\nMedium clustering coefficient:", medium_coefficient / len(p))

if __name__== "__main__" :
  main()


# The main guide for this implementation was the pseudocode found on following wikipedia page: https://en.wikipedia.org/wiki/Bron–Kerbosch_algorithm
# This Bron-Kerbosch algorithm implementation was adapted and based on the following implementation: https://stackoverflow.com/questions/13904636/implementing-bron-kerbosch-algorithm-in-python
# The medium clustering coefficient was adapted and based on the following implementation: https://stackoverflow.com/questions/58044012/how-to-calculate-clustering-coefficient-of-each-node-in-the-graph-in-python-usin