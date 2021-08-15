import GraphClass

def main():
  with open("soc-dolphins.txt") as f:
      lines = f.read().strip().split("\n")

  vertexes = []

  for line in lines:
      ls = line.split(" ")
      vertexes.append((ls[0], ls[1]))

  grafo = GraphClass.Graph(vertexes)
  print(dict.__repr__(grafo.adj))


if __name__== "__main__" :
  main()

