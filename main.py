import GraphClass

def main():
  with open("soc-dolphins.txt") as f:
      lines = f.read().strip().split("\n")

  edges = []

  for line in lines:                # Format the edges list
      ls = line.split(" ")
      edges.append((ls[0], ls[1]))

  graph = GraphClass.Graph(edges)   # Generates the graph

  p = graph.get_vertex()
  r = []
  x = []

  print("Sem pivotamento:")
  bronk(p, r, x, graph)

def bronk(p, r, x, graph):          # Executes the algorithm without pivoting
  if not any((p, x)):               # If p and x are empty, r is a maximal clique
    print(r)
  for v in p[:]:
    r2 = r + [v]
    p2 = [val for val in p if val in graph[v]]    #  P is restricted to the neighbor set of v
    x2 = [val for val in x if val in graph[v]]    #  X is restricted to the neighbor set of v
    bronk(p2, r2, x2, graph)        # Recursive call 
    p.remove(v)
    x.append(v)

if __name__== "__main__" :
  main()

