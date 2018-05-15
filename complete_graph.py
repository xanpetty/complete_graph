import sys

def complete_graph(nodes):

  connections = ( (nodes * (nodes-1)) / 2 )
  return(int(connections))


nodes = int(sys.argv[1])

connections = complete_graph(nodes)

print("number of nodes: " + str(nodes) + "\nnumber of connections: " + str(connections))
