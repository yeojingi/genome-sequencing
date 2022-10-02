def degrees(edges):
  degs = {}
  for key, value in edges.items():
    if not degs.get(key):
      degs[key] = len(value)
    else:
      degs[key] += len(value)

    for v in value:
      if not degs.get(v):
        degs[v] = -1
      else:
        degs[v] -= 1
  
  return degs