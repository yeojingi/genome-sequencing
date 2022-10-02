# EulerianCycle(Graph)
#     form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
#     while there are unexplored edges in Graph
#         select a node newStart in Cycle with still unexplored edges
#         form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking 
#         Cycle ← Cycle’
#     return Cycle

def eulerian_cycle(edges):
  stack = []
  cur = 0
  circuit = []
  numEdge = 0

  for key, value in edges.items():
    numEdge += len(value)

  while len(circuit) < numEdge:
    if len(edges[cur]) > 0:
      next = edges[cur][0]
      edges[cur].remove(next)

      stack.append(cur)
      cur = next
    else:
      circuit.append(cur)
      cur = stack.pop()
  
  circuit.append(cur)
  circuit.reverse()
  
  return circuit