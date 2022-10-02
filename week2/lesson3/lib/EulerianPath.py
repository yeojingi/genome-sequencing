def eulerian_path(edges):
  stack = []
  cur = 0
  circuit = []
  numEdge = 0
  degrees = {}

  for key, value in edges.items():
    numEdge += len(value)

    if not degrees.get(key):
      degrees[key] = -len(value)
    else:
      degrees[key] -= len(value)
    
    for e in value:
      if not degrees.get(e):
        degrees[e] = 1
      else:
        degrees[e] += 1

  odds = []
  for key, value in degrees.items():
    if value != 0:
      odds.append(key)
  
  if not edges.get(odds[0]):
    edges[odds[0]] = [odds[1]]
  else:
    edges[odds[0]].append(odds[1])
  
  # if not edges.get(odds[1]):
  #   edges[odds[1]] = [odds[0]]
  # else:
  #   edges[odds[1]].append(odds[0])

  cur = odds[0]
  numEdge += 1

  while len(circuit) < numEdge:
    if edges.get(cur) and len(edges[cur]) > 0:
      next = edges[cur][0]
      edges[cur].remove(next)

      stack.append(cur)
      cur = next
    else:
      circuit.append(cur)
      if stack:
        cur = stack.pop()
  

  ans = []
  circuit.append(cur)
  circuit.reverse()
  for i in range(len(circuit)):
    if (circuit[i] == odds[1] and circuit[i-1] == odds[0]):
      ans = circuit[:i] + circuit[i+1:]
  
  return ans