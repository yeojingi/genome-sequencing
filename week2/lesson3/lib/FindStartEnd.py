def find_start_end(edges):
  degrees = {}
  for key, value in edges.items():

    if not degrees.get(key):
      degrees[key] = -len(value)
    else:
      degrees[key] -= len(value)
    
    for e in value:
      if not degrees.get(e):
        degrees[e] = 1
      else:
        degrees[e] += 1

  candidates = []
  
  for key, value in degrees.items():
    if value != 0:
      candidates.append(key)
  
  return candidates